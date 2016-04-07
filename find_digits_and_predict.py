import matplotlib.patches as mpatches
from pylab import plt, np
from scipy.misc import imresize
from skimage.measure import regionprops


def show_prediction_result(image, label_image, clf):
    size = (8, 8)
    plt.figure(figsize=(20, 10))
    plt.imshow(image, cmap='gray_r')
    candidates = []
    predictions = []
    for region in regionprops(label_image):
        # skip small images
        #     if region.area < 100:
        #         continue
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        # make regions square
        maxwidth = np.max([maxr - minr, maxc - minc])
        minr, maxr = int(0.5 * ((maxr + minr) - maxwidth)) - 3, int(0.5 * ((maxr + minr) + maxwidth)) + 3
        minc, maxc = int(0.5 * ((maxc + minc) - maxwidth)) - 3, int(0.5 * ((maxc + minc) + maxwidth)) + 3
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2, alpha=0.2)
        plt.gca().add_patch(rect)
        # predict digit
        candidate = image[minr:maxr, minc:maxc]
        candidate = np.array(imresize(candidate, size), dtype=float)
        # invert
        # candidate = np.max(candidate) - candidate
        #     print im
        # rescale to 16 in integer
        candidate = (candidate - np.min(candidate))
        if np.max(candidate) == 0:
            continue
        candidate /= np.max(candidate)
        candidate[candidate < 0.2] = 0.0
        candidate *= 16
        candidate = np.array(candidate, dtype=int)
        prediction = clf.predict(candidate.reshape(-1))
        candidates.append(candidate)
        predictions.append(prediction)
        plt.text(minc - 10, minr - 10, "{}".format(prediction), fontsize=50)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.tight_layout()
    plt.show()
    return candidates, predictions
