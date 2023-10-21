from collections import defaultdict


def gather_credits(required_credits, *courses):
    courses_taken = defaultdict(int)
    for course_name, course_credits in courses:
        if course_name not in courses_taken:
            # if sum(courses_taken.values()) + course_credits <= required_credits:
            courses_taken[course_name] = int(course_credits)
        if sum(courses_taken.values()) >= required_credits:
            break

    if sum(courses_taken.values()) >= required_credits:
        result = (f"Enrollment finished! Maximum credits: {sum(courses_taken.values())}."
                  f"\nCourses: {', '.join(sorted(courses_taken.keys()))}")
    else:
        result = (f"You need to enroll in more courses! "
                  f"You have to gather {required_credits - sum(courses_taken.values())} credits more.")

    return result


def main():
    # print(gather_credits(80, ("Basics", 27), ))
    # print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))
    print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))


if __name__ == '__main__':
    main()
