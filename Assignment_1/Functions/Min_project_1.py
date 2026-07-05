# Accept a hyphen-separated sequence of colors
# and return the colors in alphabetical order.

def sort_colors(colors):

    color_list = colors.split("-")

    color_list.sort()

    result = "-".join(color_list)

    return result


colors = input("Enter the hyphen-separated colors: ")

print("Sorted Colors:", sort_colors(colors))
