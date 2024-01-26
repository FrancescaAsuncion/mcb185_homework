# Given values for true positives, false positives, true negatives, and false negatives, write a function that returns the accuracy and F1 score. 
# Demonstrate your function works by using it several times in the program.

def test(tp, fp, tn, fn):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	accuracy = (tp + tn) / (tp + fp + fn + tn)
	f1 = (2 * precision * recall) / (precision + recall)
	return f1, accuracy
	if tp <0: return "error read"
print(test(1,2,3,4))
print(test(0, 10, 3, 2))
print(test(4,3,2,1))