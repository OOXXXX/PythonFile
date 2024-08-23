import sys
import os.path
from format_list import format_list, format_list_or, str_time, is_initial, period_of_time, day_of_time, time_of_day

# Section 2
def file_exists(file_name):
    # Returns True if the file exists, False otherwise
    return os.path.isfile(file_name)

# Section 3
def parse_file(file_name):
    participants = []
    days = []

    if not file_exists(file_name):
        print("Error found in file, aborting.")
        sys.exit()

    with open(file_name, 'r') as file:
        # Read and clean participants' names
        participants = file.readline().strip().split(',')
        participants = [name.strip() for name in participants]

        # Read the number of days, and handle invalid data
        try:
            num_days = int(file.readline().strip())
        except ValueError:
            print("Error found in file, aborting.")
            sys.exit()

        for _ in range(num_days):
            # Read and parse the test results for the day
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

            # Read and parse the number of contact groups
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

            # Store the day's test results and groups
            days.append((tests, groups))

    return participants, days


# Section 4
def pretty_print_infiltration_data(data):
    participants, days = data

    print("Vampire Infiltration Data")
    print(f"{len(days)} days with the following participants: \
{format_list(participants)}.")

    for i, (tests, groups) in enumerate(days, start=1):
        print(f"Day {i} has {len(tests)} vampire test{'s' if len(tests) > 1 else ''} \
and {len(groups)} contact group{'s' if len(groups) > 1 else ''}.")

        # Print test results
        print(f"  {len(tests)} test{'s' if len(tests) > 1 else ''}")
        for participant in sorted(tests.keys()):
            result = "vampire!" if tests[participant] else "human."
            print(f"    {participant} is a {result}")

        # Print contact groups
        print(f"  {len(groups)} group{'s' if len(groups) > 1 else ''}")
        for group in groups:
            print(f"    {', '.join(group)}")

    print("End of Days")


# Section 5
def contacts_by_time(participant, time, contacts_daily):
    day = (time - 1) // 2  # Calculate which day
    time_of_day = time % 2  # Determine if it is AM or PM

    if day < len(contacts_daily):
        for group in contacts_daily[day]:
            if participant in group:
                return group

    return []


# Section 6
def create_initial_vk(participants):
    # Initially, all participants have an unknown status
    return {participant: "U" for participant in participants}


# Pretty-print the vampire knowledge
def pretty_print_vampire_knowledge(vk):
    humans = [name for name, status in vk.items() if status == "H"]
    vampires = [name for name, status in vk.items() if status == "V"]
    unclear = [name for name, status in vk.items() if status == "U"]

    # Print human participants
    print(f"  Humans: {format_list(humans) if humans else '(None)'}")

    # Print unclear participants
    print(f"  Unclear individuals: {format_list(unclear) if unclear else '(None)'}")

    # Print vampire participants, handling singular/plural correctly
    if len(vampires) > 1:
        print(f"  Vampires: {format_list(vampires) if vampires else '(None)'}")
    elif len(vampires) == 1:
        print(f"  Vampire: {vampires[0]}")


# Pretty-print the full vampire knowledge table
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


# Pretty-print the vampire knowledge (customized for Section 9)
def pretty_print_vampire_knowledge(vk):
    humans = [name for name, status in vk.items() if status == "H"]
    vampires = [name for name, status in vk.items() if status == "V"]
    unclear = [name for name, status in vk.items() if status == "U"]

    # Print human participants
    if len(humans) == 1:
        print(f"  Human: {humans[0]}")
    else:
        print(f"  Humans: {format_list(humans) if humans else '(None)'}")

    # Print unclear participants
    if len(unclear) == 1:
        print(f"  Unclear individual: {unclear[0]}")
    else:
        print(f"  Unclear individuals: {format_list(unclear) if unclear else '(None)'}")

    # Print vampire participants
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
    # Check mistake
    for participant, status in vk_pre.items():
        if status == "V":
            if vk_post[participant] == "H":
                print("Error found in data: vampires cannot be human; aborting.")
                sys.exit()
            vk_post[participant] = "V"
        elif status == "H" and vk_post[participant] == "V":
            print("Error found in data: humans cannot be vampires; aborting.")
            sys.exit()

    # deal with involved participant
    all_participants = set(vk_pre.keys())
    involved_participants = set()

    for group in contacts:
        for participant in group:
            if participant not in all_participants:
                print("Error found in data: contact subject is not a participant; aborting.")
                sys.exit()
            involved_participants.add(participant)

        # check if all human group
        all_human = all(vk_pre[p] == "H" for p in group)
        if all_human:
            for participant in group:
                if vk_post[participant] == "V":
                    print("Error found in data: humans cannot be vampires; aborting.")
                    sys.exit()
                vk_post[participant] = "H"

    # deal with not involved participant
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
    last_vk = vks[-1]

    for participant, status in last_vk.items():
        if status == "V":
            start = 0
            end = len(vks) - 1

            # Find the last confirmed human status
            for t in range(len(vks) - 1, -1, -1):
                if vks[t][participant] == "H":
                    start = t
                    break

            # Find the first confirmed vampire status
            for t in range(start + 1, len(vks)):
                if vks[t][participant] == "V":
                    end = t
                    break

            windows[participant] = (start, end)

    return windows

# Pretty-print the infection windows
def pretty_print_infection_windows(iw):
    for participant in sorted(iw.keys()):
        start, end = iw[participant]
        start_time = str_time(start)
        end_time = str_time(end)

        if start == 0:
            print(f"  {participant} was turned between {start_time} and {end_time}.")
        else:
            print(f"  {participant} was turned between day {start_time} and day {end_time}.")


# Section 13
def find_potential_sires(iw, groups):
    sires = {}

    for vampire, (start, end) in iw.items():
        sires[vampire] = []
        for day in range(start + 1, end + 1):
            pm_time = 2 * day  # PM time is calculated as 2 * day

            if pm_time - 1 < len(groups):
                current_groups = groups[pm_time - 1]

                contacts = [group for group in current_groups if vampire in group]

                if contacts:
                    sires[vampire].append((pm_time, contacts))
                else:
                    sires[vampire].append((pm_time, [(None)]))
            else:
                sires[vampire].append((pm_time, [(None)]))

    return sires

# Pretty-print potential sires
def pretty_print_potential_sires(ps):
    for vampire in sorted(ps.keys()):
        print(f"  {vampire}:")
        for time, contacts in ps[vampire]:
            time_str = str_time(time)
            if contacts == [(None)]:
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
                if group is None:
                    continue

                trimmed_group = []
                for participant in group:
                    if participant == vampire or vks[time][participant] == "H":
                        continue
                    trimmed_group.append(participant)

                if trimmed_group:
                    new_contacts.append(trimmed_group)

            if new_contacts:
                trimmed_ps[vampire].append((time, new_contacts))
            else:
                trimmed_ps[vampire].append((time, [(None)]))

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
                new_iw[vampire] = (0, 0)
        else:
            new_iw[vampire] = (start, end)

    return new_iw


# Section 16
def update_vks_with_windows(vks, iw):
    changes = 0

    for vampire, (start, end) in iw.items():
        # Check if the vampire status is incorrect before the infection window starts
        for t in range(0, start + 1):
            if vks[t][vampire] == "V":
                print(f"Error found in data: humans cannot be vampires; Vampire: {vampire}, Time: {t}")
                return vks, changes  # Do not exit the program, continue to see where the issue is

        # After the infection window ends, the individual should be a vampire
        for t in range(end, len(vks)):
            if vks[t][vampire] == "H":
                print(f"Error found in data: vampires cannot be humans; Vampire: {vampire}, Time: {t}")
                return vks, changes  # Do not exit the program, continue running

            if vks[t][vampire] == "U":
                vks[t][vampire] = "V"
                changes += 1

    return vks, changes


# Section 17
def cyclic_analysis(vks, iw, ps):
    count = 0
    changes = 1
    max_iterations = 100  # Set a maximum iteration count to prevent infinite loops

    while changes != 0 and count < max_iterations:
        ps = trim_potential_sires(ps, vks)
        iw = trim_infection_windows(iw, ps)
        vks, changes = update_vks_with_windows(vks, iw)
        count += 1

    if count >= max_iterations:
        print("Warning: cyclic_analysis reached maximum iterations without converging.")

    return vks, iw, ps, count


# Section 18
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

    return originals, unclear_vamps, newborns


# Pretty-print the vampire strata
def pretty_print_vampire_strata(originals, unclear_vamps, newborns):
    print(f"  Original vampires: {', '.join(sorted(originals)) if originals else '(None)'}")
    print(f"  Unknown strata vampires: {', '.join(sorted(unclear_vamps)) if unclear_vamps else '(None)'}")
    print(f"  Newborn vampires: {', '.join(sorted(newborns)) if newborns else '(None)'}")


# Section 19
def calculate_sire_sets(ps):
    ss = {}

    for vampire, time_groups in ps.items():
        sires = set()
        for time, groups in time_groups:
            if time is not None:
                for group in groups:
                    sires.update(group)
        # Remove the vampire themselves from the sire set
        sires.discard(vampire)
        ss[vampire] = sires

    return ss


# Pretty-print the sire sets
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


# Section 20
def find_hidden_vampires(ss, iw, vamps, vks):
    changes = 0

    for vampire in vamps:
        sires = ss[vampire]

        if len(sires) == 1:
            sire = next(iter(sires))  # Get the only potential sire
            start, end = iw[vampire]

            # Propagate the sire's vampire status forward
            for t in range(end, len(vks)):
                if vks[t][sire] == "H":
                    print("Error found in data: vampires cannot be humans; aborting.")
                    sys.exit()
                if vks[t][sire] == "U":
                    vks[t][sire] = "V"
                    changes += 1

            # Ensure the sire was a vampire right before the infection window ends
            if end > 0:
                if vks[end - 1][sire] == "H":
                    print("Error found in data: vampires cannot be humans; aborting.")
                    sys.exit()
                if vks[end - 1][sire] == "U":
                    vks[end - 1][sire] = "V"
                    changes += 1

    return vks, changes

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