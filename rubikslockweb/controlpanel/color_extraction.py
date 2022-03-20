import cv2

from controlpanel.color_ranges import get_components, get_mapped_face

class cell:
    def __init__(self):
        self.x = None
        self.y = None
        self.cX = None
        self.cY = None
        self.w = None
        self.h = None
        self.label = None

def get_face(img):
# img = cv2.imread('imgs/2.jpg')

	scale_percent = 25# percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	
	# resize image
	img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

	(numLabels, labels, stats, centroids) = get_components(img)

	cells = []

	for i in range(0, numLabels):
		if i:
			current_cell = cell()
			current_cell.x = stats[i, cv2.CC_STAT_LEFT]
			current_cell.y = stats[i, cv2.CC_STAT_TOP]
			current_cell.w = stats[i, cv2.CC_STAT_WIDTH]
			current_cell.h = stats[i, cv2.CC_STAT_HEIGHT]
			current_cell.label = i
			current_cell.cX = int(centroids[i][0])
			current_cell.cY = int(centroids[i][1])

			cells.append(current_cell)

	sorted_cells = sorted(cells, key = lambda cell: cell.cY)
	mapped_cells = [
		*sorted(sorted_cells[:3], key = lambda cell: cell.cX), 
		*sorted(sorted_cells[3:6], key = lambda cell: cell.cX), 
		*sorted(sorted_cells[6:], key = lambda cell: cell.cX)
	]

	# cv2.imshow("Original", img)

	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return get_mapped_face(img, mapped_cells)
