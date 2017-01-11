def largest_histogram(histogram):
    histogram.append(0)
    max_line = 0
    for elem in histogram:
        count = 0
        for a in histogram:
            if a >= elem:
                count += 1
            else:
                if count * elem > max_line:
                    max_line = count * elem
                count = 0
    return max_line

if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

