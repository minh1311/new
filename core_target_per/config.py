conf_threshold = 0.3
iou_threshold = 0.3
device = "gpu"
model_path_detect = "./assets/yolo11m640.onnx"


track_thresh = 0.3
match_thresh = 0.8
track_buffer = 50


frame_rate=50
# polygons_list = [[(616, 170), (843, 126), (885, 264), (662, 308)]]
polygons_list = [[(796, 337), (1174, 314), (1245, 856), (835, 895)]]


# Danh sách để lưu các polygon
# polygon config video quan mt
# [[(579, 478), (825, 469), (812, 730), (582, 740)], [(913, 534), (1221, 528), (1242, 756), (898, 746)], [(816, 360), (1064, 368), (1074, 499), (843, 509)]]
