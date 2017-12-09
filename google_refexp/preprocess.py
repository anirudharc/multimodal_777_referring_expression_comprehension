import numpy as np
import cPickle as cp
import json

train_data = json.load(open('google_refexp_train_201511_coco_aligned_multibox_umd.json'))
val_data = json.load(open('google_refexp_val_201511_coco_aligned_multibox_umd.json'))

train_images = ['dataset/' + image_id for image_id in train_data['images']]
val_images = ['dataset/' + image_id for image_id in val_data['images']]

train_images_filename = ['dataset/' + train_data['images'][image_id]['file_name'] for image_id in train_data['images']]
val_images_filename = ['dataset/' + val_data['images'][image_id]['file_name'] for image_id in val_data['images']]

train_bboxes_list = []
for image_id in train_data['images']:
	a = np.zeros((len(train_data['images'][image_id]['region_candidates']), 6))
	for (i, bbox) in enumerate(train_data['images'][image_id]['region_candidates']):
		a[i, :] = [bbox['bounding_box'][0], bbox['bounding_box'][1], bbox['bounding_box'][0]+bbox['bounding_box'][2], bbox['bounding_box'][1]+bbox['bounding_box'][3], 1.0, 0]
		train_bboxes_list.append(a)

val_bboxes_list = []
for image_id in val_data['images']:
	a = np.zeros((len(val_data['images'][image_id]['region_candidates']), 6))
	for (i, bbox) in enumerate(val_data['images'][image_id]['region_candidates']):
		a[i, :] = [bbox['bounding_box'][0], bbox['bounding_box'][1], bbox['bounding_box'][0]+bbox['bounding_box'][2], bbox['bounding_box'][1]+bbox['bounding_box'][3], 1.0, 0]
		val_bboxes_list.append(a)

json.dump(train_images, open('images_input_train.json', 'w'))
json.dump(val_images, open('images_input_val.json', 'w'))

json.dump(train_images_filename, open('images_input_train_filename.json', 'w'))
json.dump(val_images_filename, open('images_input_val_filename.json', 'w'))

cp.dump(train_bboxes_list, open('bboxes_input_train.cp', 'w'))
cp.dump(train_bboxes_list, open('bboxes_input_val.cp', 'w'))