def main():
    larger_box = {
        "x1" : 0,
        "y1" : 0,
        "x2" : 50,
        "y2" : 50
    }
    smaller_box = {
        "x1" : -10,
        "y1" : 10,
        "x2" : 60,
        "y2" : 20
    }
    print(get_overlap_perc(larger_box, smaller_box)) 

def get_overlap_perc(larger, smaller):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    assert larger['x1'] < larger['x2']
    assert larger['y1'] < larger['y2']
    assert smaller['x1'] < smaller['x2']
    assert smaller['y1'] < smaller['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(larger['x1'], smaller['x1'])
    y_top = max(larger['y1'], smaller['y1'])
    x_right = min(larger['x2'], smaller['x2'])
    y_bottom = min(larger['y2'], smaller['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    larger_area = (larger['x2'] - larger['x1']) * (larger['y2'] - larger['y1'])
    smaller_area = (smaller['x2'] - smaller['x1']) * (smaller['y2'] - smaller['y1'])

    # Two ways to calculate a percentage error 
    # percentage within the smaller rectangle (or "self" in your program), the percent overlap is:
    iou = intersection_area / smaller_area
    return iou
    
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    # percentage to be equal whether it's calculated from either rectangle
    # iou = intersection_area / float(larger_area + smaller_area - intersection_area)
    # assert iou >= 0.0
    # assert iou <= 1.0
    # return iou


if __name__ == "__main__":
    main()
