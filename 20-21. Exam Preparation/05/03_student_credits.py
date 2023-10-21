def students_credits(*course_curriculum):
    course_results = {}
    for course in course_curriculum:
        course_name, course_credits, max_test_points, diyan_test_points = course.split('-')
        diyan_course_credits = int(course_credits) * (int(diyan_test_points) / int(max_test_points))
        course_results[course_name] = diyan_course_credits

    total_credits = sum(course_results.values())
    diploma_threshold = 240

    if total_credits >= diploma_threshold:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:
        result = f"Diyan needs {diploma_threshold - total_credits:.1f} credits more for a diploma."

    for course_name, course_credits in sorted(course_results.items(), key=lambda kvp: -kvp[1]):
        result += f"\n{course_name} - {course_credits:.1f}"

    return result


def main():
    # print(students_credits("Computer Science-12-300-250", "Basic Algebra-15-400-200", "Algorithms-25-500-490"))
    print(students_credits(
            "Discrete Maths-40-500-450",
            "AI Development-20-400-400",
            "Algorithms Advanced-50-700-630",
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Game Engine Development-70-100-70",
            "Mobile Development-25-250-225",
            "QA-20-300-300",
        )
    )


if __name__ == '__main__':
    main()