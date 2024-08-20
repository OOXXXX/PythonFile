import sys
import os.path
from format_list import format_list, format_list_or, str_time, is_initial, period_of_time, day_of_time, time_of_day


# Section 2
def file_exists(file_name):
    # 检查文件是否存在
    return os.path.isfile(file_name)

# Section 3
def parse_file(file_name):
    participants = []
    days = []

    # 检查文件是否存在
    if not file_exists(file_name):
        print("Error found in file, aborting.")
        sys.exit()  # 直接退出程序而不是返回空列表

    with open(file_name, 'r') as file:
        # 读取参与者名单，并去除空白字符
        participants = file.readline().strip().split(',')
        participants = [name.strip() for name in participants]

        # 读取天数
        try:
            num_days = int(file.readline().strip())
        except ValueError:
            print("Error found in file, aborting.")
            sys.exit()

        for _ in range(num_days):
            # 解析当天的测试结果
            tests = {}
            test_line = file.readline().strip()
            if test_line != "##":
                test_entries = test_line.split(',')
                for entry in test_entries:
                    try:
                        name, result = entry.split(':')
                        tests[name.strip()] = result.strip() == 'V'
                    except ValueError:
                        print("Error found in file, aborting.")
                        sys.exit()

            # 解析当天的接触组
            try:
                num_groups = int(file.readline().strip())
            except ValueError:
                print("Error found in file, aborting.")
                sys.exit()

            groups = []
            for _ in range(num_groups):
                group = file.readline().strip().split(',')
                group = [name.strip() for name in group]
                groups.append(group)

            # 将测试结果和接触组存入days列表
            days.append((tests, groups))

    return (participants, days)


# Section 4
def pretty_print_infiltration_data(data):
    participants, days = data

    print(f"Vampire Infiltration Data")
    print(f"{len(days)} days with the following participants: {', '.join(participants[:-1])} and {participants[-1]}.")

    for i, (tests, groups) in enumerate(days, start=1):
        print(f"Day {i} has {len(tests)} vampire test{'s' if len(tests) > 1 else ''} and {len(groups)} contact group{'s' if len(groups) > 1 else ''}.")

        print(f"  {len(tests)} test{'s' if len(tests) > 1 else ''}")
        for participant in sorted(tests.keys()):
            result = "vampire!" if tests[participant] else "human."
            print(f"    {participant} is a {result}")

        print(f"  {len(groups)} group{'s' if len(groups) > 1 else ''}")
        for group in groups:
            print(f"    {', '.join(group)}")

    print("End of Days")


# Section 5
def contacts_by_time(participant, time, contacts_daily):
    day = (time - 1) // 2  # 计算出是哪一天
    time_of_day = time % 2  # 判断是AM还是PM

    if day < len(contacts_daily):
        # AM时间段
        if time_of_day == 1:
            for group in contacts_daily[day]:
                if participant in group:
                    return group
        # PM时间段
        elif time_of_day == 0:
            for group in contacts_daily[day]:
                if participant in group:
                    return group

    return []


# Section 6
def create_initial_vk(participants):
    vk = {participant: "U" for participant in participants}
    return vk


def pretty_print_vampire_knowledge(vk):
    humans = [name for name, status in vk.items() if status == "H"]
    vampires = [name for name, status in vk.items() if status == "V"]
    unclear = [name for name, status in vk.items() if status == "U"]

    print(f"  Humans: {format_list(humans) if humans else '(None)'}")
    print(f"  Unclear individuals: {format_list(unclear) if unclear else '(None)'}")

    # 仅在吸血鬼数量大于1时显示 "Vampires" 部分
    if len(vampires) > 1:
        print(f"  Vampires: {format_list(vampires) if vampires else '(None)'}")
    elif len(vampires) == 1:
        print(f"  Vampire: {vampires[0]}")

# Done by professors
def pretty_print_vks(vks):
    print(f'Vampire Knowledge Tables')
    for i in range(len(vks)):
        print(f'Day {str_time(i)}:')
        pretty_print_vampire_knowledge(vks[i])
    print(f'End Vampire Knowledge Tables')


# Section 7
def update_vk_with_tests(vk, tests):
    for participant, result in tests.items():
        if participant not in vk:
            print("Error found in data: test subject is not a participant; aborting.")
            sys.exit()

        current_status = vk[participant]

        if current_status == "U":
            vk[participant] = "V" if result else "H"
        elif current_status == "H" and result:
            print("Error found in data: humans cannot be vampires; aborting.")
            sys.exit()
        elif current_status == "V" and not result:
            print("Error found in data: vampires cannot be humans; aborting.")
            sys.exit()

    return vk


# Section 8
def update_vk_with_vampires_forward(vk_pre, vk_post):
    for participant, status in vk_pre.items():
        if status == "V":
            if vk_post[participant] == "H":
                print("Error found in data: vampires cannot be humans; aborting.")
                sys.exit()
            elif vk_post[participant] == "U":
                vk_post[participant] = "V"

    return vk_post


# Section 9
def update_vk_with_humans_backward(vk_pre, vk_post):
    for participant, status in vk_post.items():
        if status == "H":
            if vk_pre[participant] == "V":
                print("Error found in data: humans cannot be vampires; aborting.")
                sys.exit()
            elif vk_pre[participant] == "U":
                vk_pre[participant] = "H"

    return vk_pre

def pretty_print_vampire_knowledge(vk):
    humans = [name for name, status in vk.items() if status == "H"]
    vampires = [name for name, status in vk.items() if status == "V"]
    unclear = [name for name, status in vk.items() if status == "U"]

    if len(humans) == 1:
        print(f"  Human: {humans[0]}")
    else:
        print(f"  Humans: {format_list(humans) if humans else '(None)'}")

    if len(unclear) == 1:
        print(f"  Unclear individual: {unclear[0]}")
    else:
        print(f"  Unclear individuals: {format_list(unclear) if unclear else '(None)'}")

    if len(vampires) == 1:
        print(f"  Vampire: {vampires[0]}")
    elif len(vampires) > 1:
        print(f"  Vampires: {format_list(vampires)}")
    else:
        print(f"  Vampires: (None)")

# Section 10
def update_vk_overnight(vk_pre, vk_post):
    for participant, status in vk_pre.items():
        if status == "H":
            if vk_post[participant] == "V":
                print("Error found in data: humans cannot be vampires; aborting.")
                sys.exit()
            vk_post[participant] = "H"
        elif status == "V":
            if vk_post[participant] == "H":
                print("Error found in data: vampires cannot be humans; aborting.")
                sys.exit()
            vk_post[participant] = "V"

    return vk_post


# Section 11
def update_vk_with_contact_group(vk_pre, contacts, vk_post):
    # 检查错误并传播吸血鬼状态
    for participant, status in vk_pre.items():
        if status == "V":
            if vk_post[participant] == "H":
                print("Error found in data: vampires cannot be human; aborting.")
                sys.exit()
            vk_post[participant] = "V"
        elif status == "H" and vk_post[participant] == "V":
            print("Error found in data: humans cannot be vampires; aborting.")
            sys.exit()

    # 处理接触组
    all_participants = set(vk_pre.keys())
    involved_participants = set()

    for group in contacts:
        for participant in group:
            if participant not in all_participants:
                print("Error found in data: contact subject is not a participant; aborting.")
                sys.exit()
            involved_participants.add(participant)

        # 检查是否为全人类组
        all_human = all(vk_pre[p] == "H" for p in group)
        if all_human:
            for participant in group:
                if vk_post[participant] == "V":
                    print("Error found in data: humans cannot be vampires; aborting.")
                    sys.exit()
                vk_post[participant] = "H"

    # 处理未参与接触组的参与者
    for participant in all_participants - involved_participants:
        if vk_pre[participant] == "H":
            if vk_post[participant] == "V":
                print("Error found in data: humans cannot be vampires; aborting.")
                sys.exit()
            vk_post[participant] = "H"

    return vk_post


# Section 12
def find_infection_windows(vks):
    windows = {}

    # 获取最后一个时间段的 vk 结构
    last_vk = vks[-1]

    # 找出所有最后一个时间段的吸血鬼
    for participant, status in last_vk.items():
        if status == "V":
            start = 0
            end = len(vks) - 1

            # 回溯找到最后的确切人类状态
            for t in range(len(vks) - 1, -1, -1):
                if vks[t][participant] == "H":
                    start = t
                    break

            # 找到首次被确认吸血
            for t in range(start + 1, len(vks)):
                if vks[t][participant] == "V":
                    end = t
                    break

            windows[participant] = (start, end)

    return windows

def pretty_print_infection_windows(iw):
    for participant in sorted(iw.keys()):
        start, end = iw[participant]
        start_time = str_time(start)
        end_time = str_time(end)
        print(f"  {participant} was turned between {start_time} and {end_time}.")


# Section 13
def find_potential_sires(iw, groups):
    sires = {}

    for vampire, (start, end) in iw.items():
        sires[vampire] = []

        for day in range(start + 1, end + 1):
            pm_time = 2 * day  # PM时间为2 * day
            if pm_time - 1 < len(groups):
                pm_groups = groups[pm_time - 1]

                # 查找吸血鬼当天的接触组
                contacts = [group for group in pm_groups if vampire in group]

                if contacts:
                    sires[vampire].append((pm_time, contacts))
                else:
                    sires[vampire].append((pm_time, [(None)]))  # 如果吸血鬼当天没有任何接触，添加一个空记录

    return sires

def pretty_print_potential_sires(ps):
    for vampire in sorted(ps.keys()):
        print(f"  {vampire}:")
        for time, contacts in ps[vampire]:
            time_str = str_time(time)
            if not contacts or contacts == [(None)]:
                print(f"    On {time_str}, met with (None).")
            else:
                for group in contacts:
                    contact_list = ', '.join(sorted(group))
                    print(f"    On {time_str}, met with {contact_list}.")


# Section 14
def trim_potential_sires(ps, vks):
    trimmed_ps = {}

    for vampire, contact_days in ps.items():
        trimmed_ps[vampire] = []

        for time, contacts in contact_days:
            new_contacts = []

            for group in contacts:
                trimmed_group = []
                for participant in group:
                    # 去除吸血鬼自己
                    if participant == vampire:
                        continue

                    # 去除已确认是人类的参与者
                    if vks[time][participant] == "H":
                        continue

                    trimmed_group.append(participant)

                # 如果精简后的组不为空，则添加到新的联系人组中
                if trimmed_group:
                    new_contacts.append(trimmed_group)

            # 如果新的联系人列表不为空，则添加到精简后的结果中
            if new_contacts:
                trimmed_ps[vampire].append((time, new_contacts))
            else:
                trimmed_ps[vampire].append((time, [(None)]))  # 如果所有联系人都被过滤掉了，保留空记录

    return trimmed_ps


# Section 15
def trim_infection_windows(iw, ps):
    new_iw = {}

    for vampire, (start, end) in iw.items():
        if vampire in ps:
            sire_times = [time for time, contacts in ps[vampire] if contacts != [(None)]]

            if sire_times:
                new_start = min(sire_times)
                new_end = max(sire_times)
                new_iw[vampire] = (new_start, new_end)
            else:
                # 如果没有潜在的感染者，窗口收紧为 (0, 0)
                new_iw[vampire] = (0, 0)
        else:
            # 保持原来的感染窗口
            new_iw[vampire] = (start, end)

    return new_iw


# Section 16
def update_vks_with_windows(vks, iw):
    changes = 0

    for vampire, (start, end) in iw.items():
        # 在窗口开始前，吸血鬼应该是人类
        for t in range(0, start + 1):
            if vks[t][vampire] == "V":
                print("Error found in data: humans cannot be vampires; aborting.")
                sys.exit()
            if vks[t][vampire] == "U":
                vks[t][vampire] = "H"
                changes += 1

        # 在窗口结束后，吸血鬼应该是吸血鬼
        for t in range(end, len(vks)):
            if vks[t][vampire] == "H":
                print("Error found in data: vampires cannot be humans; aborting.")
                sys.exit()
            if vks[t][vampire] == "U":
                vks[t][vampire] = "V"
                changes += 1

    return (vks, changes)


# Section 17; done by professors
def cyclic_analysis(vks, iw, ps):
    count = 0
    changes = 1
    while (changes != 0):
        ps = trim_potential_sires(ps, vks)
        iw = trim_infection_windows(iw, ps)
        (vks, changes) = update_vks_with_windows(vks, iw)
        count = count + 1
    return (vks, iw, ps, count)


# Section 18: vampire strata
def vampire_strata(iw):
    originals = set()
    unclear_vamps = set()
    newborns = set()

    for vampire, (start, end) in iw.items():
        if start == 0 and end == 0:
            originals.add(vampire)
        elif start > 0 and end > 0:
            newborns.add(vampire)
        else:
            unclear_vamps.add(vampire)

    return (originals, unclear_vamps, newborns)


def pretty_print_vampire_strata(originals, unclear_vamps, newborns):
    print(f"  Original vampires: {', '.join(sorted(originals)) if originals else '(None)'}")
    print(f"  Unknown strata vampires: {', '.join(sorted(unclear_vamps)) if unclear_vamps else '(None)'}")
    print(f"  Newborn vampires: {', '.join(sorted(newborns)) if newborns else '(None)'}")


# Section 19: vampire sire sets
def calculate_sire_sets(ps):
    ss = {}

    for vampire, time_groups in ps.items():
        sires = set()
        for time, groups in time_groups:
            if time is not None:
                for group in groups:
                    sires.update(group)
        # 移除吸血鬼自己
        sires.discard(vampire)
        ss[vampire] = sires

    return ss

def pretty_print_sire_sets(ss, iw, vamps, newb):
    if newb:
        print("  Newborn vampires:")
    else:
        print("  Vampires of unknown strata:")

    for vampire in sorted(vamps):
        sires = sorted(ss[vampire])
        start, end = iw[vampire]

        if len(sires) == 1:
            sire_str = sires[0]
        else:
            sire_str = format_list_or(sires)

        if start == end:
            print(f"    {vampire} was sired by {sire_str} on {str_time(start)}.")
        else:
            print(f"    {vampire} could have been sired by {sire_str} between {str_time(start)} and {str_time(end)}.")


# Section 20: vampire sire sets
def find_hidden_vampires(ss, iw, vamps, vks):
    changes = 0

    for vampire in vamps:
        sires = ss[vampire]

        if len(sires) == 1:
            sire = next(iter(sires))  # 唯一的感染者
            start, end = iw[vampire]

            # 将感染者的状态传播到感染窗口的末尾
            for t in range(end, len(vks)):
                if vks[t][sire] == "H":
                    print("Error found in data: vampires cannot be humans; aborting.")
                    sys.exit()
                if vks[t][sire] == "U":
                    vks[t][sire] = "V"
                    changes += 1

            # 确保感染者在感染窗口前一个时间点也是吸血鬼
            if end > 0:
                if vks[end - 1][sire] == "H":
                    print("Error found in data: vampires cannot be humans; aborting.")
                    sys.exit()
                if vks[end - 1][sire] == "U":
                    vks[end - 1][sire] = "V"
                    changes += 1

    return (vks, changes)


# Section 21; done by professor
def cyclic_analysis2(vks, groups):
    count = 0
    changes = 1
    while (changes != 0):
        iw = find_infection_windows(vks)
        ps = find_potential_sires(iw, groups)
        vks, iw, ps, countz = cyclic_analysis(vks, iw, ps)
        o, u, n = vampire_strata(iw)
        ss = calculate_sire_sets(ps)
        vks, changes = find_hidden_vampires(ss, iw, n, vks)
        count = count + 1
    return (vks, iw, ps, ss, o, u, n, count)


def main():
    """Main logic for the program.  Do not change this (although if
       you do so for debugging purposes that's ok if you later change
       it back...)
    """
    filename = ""
    # Get the file name from the command line or ask the user for a file name
    args = sys.argv[1:]
    if len(args) == 0:
        filename = input("Please enter the name of the file: ")
    elif len(args) == 1:
        filename = args[0]
    else:
        print("""\n\nUsage\n\tTo run the program type:
        \tpython contact.py infile
        where infile is the name of the file containing the data.\n""")
        sys.exit()

    # Section 2. Check that the file exists
    if not file_exists(filename):
        print("File does not exist, ending program.")
        sys.exit()

    # Section 3. Create contacts dictionary from the file
    # Complete function parse_file().
    data = parse_file(filename)
    participants, days = data
    tests_by_day = [d[0] for d in days]
    groups_by_day = [d[1] for d in days]

    # Section 4. Print contact records
    pretty_print_infiltration_data(data)

    # Section 5. Create helper function for time analysis.
    print("********\nSection 5: Lookup helper function")
    if len(participants) == 0:
        print("  No participants.")
    else:
        p = participants[0]
        if len(days) > 1:
            d = 2
        elif len(days) == 1:
            d = 1
        else:
            d = 0
        t = time_of_day(d, True)
        t2 = time_of_day(d, False)
        print(
            f"  {p}'s contacts for time unit {t} (day {day_of_time(t)}) are {format_list(contacts_by_time(p, t, groups_by_day))}.")
        print(
            f"  {p}'s contacts for time unit {t2} (day {day_of_time(t2)}) are {format_list(contacts_by_time(p, t2, groups_by_day))}.")

    # Section 6.  Create the initial data structure and pretty-print it.
    print("********\nSection 6: create initial vampire knowledge tables")
    vks = [create_initial_vk(participants) for i in range(1 + (2 * len(days)))]
    pretty_print_vks(vks)

    # Section 7.  Update the VKs with test results.
    print("********\nSection 7: update the vampire knowledge tables with test results")
    for t in range(1, len(vks), 2):
        vks[t] = update_vk_with_tests(vks[t], tests_by_day[day_of_time(t) - 1])
    pretty_print_vks(vks)

    # Section 8.  Update the VKs to push vampirism forwards in time.
    print("********\nSection 8: update the vampire knowledge tables by forward propagation of vampire status")
    for t in range(1, len(vks)):
        vks[t] = update_vk_with_vampires_forward(vks[t - 1], vks[t])
    pretty_print_vks(vks)

    # Section 9.  Update the VKs to push humanism backwards in time.
    print("********\nSection 9: update the vampire knowledge tables by backward propagation of human status")
    for t in range(len(vks) - 1, 0, -1):
        vks[t - 1] = update_vk_with_humans_backward(vks[t - 1], vks[t])
    pretty_print_vks(vks)

    # Sections 10 and 11.  Update the VKs to account for contact groups and safety at night.
    print(
        "********\nSections 10 and 11: update the vampire knowledge tables by forward propagation of contact results and overnight")
    for t in range(1, len(vks), 2):
        vks[t + 1] = update_vk_with_contact_group(vks[t], groups_by_day[day_of_time(t) - 1], vks[t + 1])
        if t + 2 < len(vks):
            vks[t + 2] = update_vk_overnight(vks[t + 1], vks[t + 2])
    pretty_print_vks(vks)

    # Section 12. Find infection windows for vampires.
    print("********\nSection 12: Vampire infection windows")
    iw = find_infection_windows(vks)
    pretty_print_infection_windows(iw)

    # Section 13. Find possible vampire sires.
    print("********\nSection 13: Find possible vampire sires")
    ps = find_potential_sires(iw, groups_by_day)
    pretty_print_potential_sires(ps)

    # Section 14. Trim the potential sire structure.
    print("********\nSection 14: Trim potential sire structure")
    ps = trim_potential_sires(ps, vks)
    pretty_print_potential_sires(ps)

    # Section 15. Trim the infection windows.
    print("********\nSection 15: Trim infection windows")
    iw = trim_infection_windows(iw, ps)
    pretty_print_infection_windows(iw)

    # Section 16. Update the vk structures with infection windows.
    print("********\nSection 16: Update vampire information tables with infection window data")
    (vks, changes) = update_vks_with_windows(vks, iw)
    pretty_print_vks(vks)
    str_s = "" if changes == 1 else "s"
    print(f'({changes} change{str_s})')

    # Section 17.  Cyclic analysis for sections 14-16
    print("********\nSection 17: Cyclic analysis for sections 14-16")
    vks, iw, ps, count = cyclic_analysis(vks, iw, ps)
    str_s = "" if count == 1 else "s"
    print(f'Detected fixed point after {count} iteration{str_s}.')
    print('Potential sires:')
    pretty_print_potential_sires(ps)
    print('Infection windows:')
    pretty_print_infection_windows(iw)
    pretty_print_vks(vks)

    # Section 18.  Calculate vampire strata
    print("********\nSection 18: Calculate vampire strata")
    (origs, unkns, newbs) = vampire_strata(iw)
    pretty_print_vampire_strata(origs, unkns, newbs)

    # Section 19.  Calculate definite sires
    print("********\nSection 19: Calculate definite vampire sires")
    ss = calculate_sire_sets(ps)
    pretty_print_sire_sets(ss, iw, unkns, False)
    pretty_print_sire_sets(ss, iw, newbs, True)

    # Section 20.  Find hidden vampires
    print("********\nSection 20: Find hidden vampires")
    (vks, changes) = find_hidden_vampires(ss, iw, newbs, vks)
    pretty_print_vks(vks)
    str_s = "" if changes == 1 else "s"
    print(f'({changes} change{str_s})')

    # Section 21.  Cyclic analysis for sections 14-20
    print("********\nSection 21: Cyclic analysis for sections 14-20")
    (vks, iw, ps, ss, o, u, n, count) = cyclic_analysis2(vks, groups_by_day)
    str_s = "" if count == 1 else "s"
    print(f'Detected fixed point after {count} iteration{str_s}.')
    print("Infection windows:")
    pretty_print_infection_windows(iw)
    print("Vampire potential sires:")
    pretty_print_potential_sires(ps)
    print("Vampire strata:")
    pretty_print_vampire_strata(o, u, n)
    print("Vampire sire sets:")
    pretty_print_sire_sets(ss, iw, u, False)
    pretty_print_sire_sets(ss, iw, n, True)
    pretty_print_vks(vks)


if __name__ == "__main__":
    main()



