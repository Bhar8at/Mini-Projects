import numpy as np
import cv2

def order_points(pts):
    # Add debugging print to see input points
    print("Input points before ordering:", pts)
    
    rect = np.zeros((4, 2), dtype="float32")
    
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)
    
    # Add more robust point ordering with error checking
    try:
        rect[0] = pts[np.argmin(s)]    # top-left
        rect[2] = pts[np.argmax(s)]    # bottom-right
        rect[1] = pts[np.argmin(diff)] # top-right
        rect[3] = pts[np.argmax(diff)] # bottom-left
        
        # Add debugging print to see ordered points
        print("Ordered points:", rect)
        
        # Verify points are in correct order by checking distances
        width1 = np.linalg.norm(rect[0] - rect[1])
        width2 = np.linalg.norm(rect[2] - rect[3])
        height1 = np.linalg.norm(rect[0] - rect[3])
        height2 = np.linalg.norm(rect[1] - rect[2])
        
        print(f"Widths: {width1:.2f}, {width2:.2f}")
        print(f"Heights: {height1:.2f}, {height2:.2f}")
        
        # Sanity check for reasonable aspect ratio
        aspect_ratio = max(width1, width2) / max(height1, height2)
        if not (0.5 <= aspect_ratio <= 2.0):
            print(f"Warning: Unusual aspect ratio detected: {aspect_ratio:.2f}")
            
    except Exception as e:
        print(f"Error in point ordering: {e}")
        raise
        
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Print original image dimensions
    print(f"Original image dimensions: {image.shape}")
    
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    print(f"Calculated output dimensions: {maxWidth}x{maxHeight}")
    
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    
    try:
        # Print matrices for debugging
        print("Source points:\n", rect)
        print("Destination points:\n", dst)
        
        M = cv2.getPerspectiveTransform(rect, dst)
        print("Transform matrix:\n", M)
        
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        
        # Check output image statistics
        print(f"Output image mean value: {np.mean(warped)}")
        print(f"Output image min/max values: {np.min(warped)}/{np.max(warped)}")
        
        # If the image is too dark, try normalizing it
        if np.mean(warped) < 30:  # arbitrary threshold
            print("Attempting to normalize dark image...")
            warped = cv2.normalize(warped, None, 0, 255, cv2.NORM_MINMAX)
        
        return warped
        
    except Exception as e:
        print(f"Error in perspective transform: {e}")
        return image 