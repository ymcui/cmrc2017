# -*- coding: UTF-8 -*-
import string
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

prediction_file = open(sys.argv[1], 'rb')
reference_file = open(sys.argv[2], 'rb')

# read reference file
reference_dict = dict()
reference_lines = reference_file.readlines()
total_count = len(reference_lines)
for line in reference_lines:
	line = line.decode('utf-8').strip()
	qid, answer = line.split(' ||| ')
	reference_dict[qid] = answer


# read prediction file
right_count = 0
for line in prediction_file.readlines():
	line = line.decode('utf-8').strip()
	line_segs = line.split(' ||| ')
	if len(line_segs) == 1:
		qid = line_segs[0]
		answer = ''
	else:
		qid = line_segs[0]
		answer = line_segs[1]
	if answer == reference_dict[qid]:
		right_count += 1

# output result
accuracy = 100.0*right_count / total_count
print('[Evaluate Script]')
print('Total predicted count ||| {}'.format(total_count))
print('Total right count     ||| {}'.format(right_count))
print('Accuracy              ||| {}'.format(accuracy))
