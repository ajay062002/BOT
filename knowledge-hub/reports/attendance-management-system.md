# Graph Report - attendance-management-system  (2026-07-10)

## Corpus Check
- 15 files · ~16,058 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 158 nodes · 238 edges · 12 communities (10 shown, 2 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c1367b65`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- facenet.py
- detect_face.py
- Network
- recognizer.py
- main.py
- Attendance Management System
- user_interface.py
- TkinterCustomButton
- align_dataset_mtcnn.py

## God Nodes (most connected - your core abstractions)
1. `Network` - 18 edges
2. `Attendance Management System` - 12 edges
3. `recognize()` - 10 edges
4. `TkinterCustomButton` - 9 edges
5. `detect_face()` - 8 edges
6. `bulk_detect_face()` - 8 edges
7. `ImageClass` - 7 edges
8. `s_exit()` - 6 edges
9. `train()` - 5 edges
10. `create_mtcnn()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `recognize()`  [EXTRACTED]
  main.py → pipeline/recognizer.py
- `recognize()` --calls--> `FaceAligner`  [INFERRED]
  pipeline/recognizer.py → src/face_detection/face_aligner.py
- `_predict_and_draw()` --calls--> `mark_present()`  [INFERRED]
  pipeline/recognizer.py → src/utils/sheet.py
- `main()` --calls--> `dataset_creation()`  [EXTRACTED]
  main.py → pipeline/dataset.py
- `main()` --calls--> `train()`  [EXTRACTED]
  main.py → pipeline/trainer.py

## Import Cycles
- None detected.

## Communities (12 total, 2 thin omitted)

### Community 0 - "facenet.py"
Cohesion: 0.07
Nodes (26): calculate_accuracy(), calculate_roc(), calculate_val(), calculate_val_far(), center_loss(), create_input_pipeline(), crop(), distance() (+18 more)

### Community 1 - "detect_face.py"
Cohesion: 0.13
Nodes (23): bbreg(), bulk_detect_face(), create_mtcnn(), detect_face(), generateBoundingBox(), imresample(), layer(), nms() (+15 more)

### Community 2 - "Network"
Cohesion: 0.17
Nodes (8): object, Network, Returns the current network output., Returns an index-suffixed unique name for the given prefix.         This is used, Creates a new TensorFlow variable., Verifies that the padding is one of the supported ones., Construct the network., Set the input(s) for the next operation by replacing the terminal nodes.

### Community 3 - "recognizer.py"
Cohesion: 0.20
Nodes (10): _detect_faces(), _embed_faces(), _predict_and_draw(), _preprocess(), recognizer.py — real-time face recognition via webcam, video, or image batch. Dr, mode: 'w' = webcam, 'v' = video, 'i' = image folder     Returns comma-separated, recognize(), _setup_output_images_folder() (+2 more)

### Community 4 - "main.py"
Cohesion: 0.23
Nodes (11): main(), main.py — entry point for the attendance management system. Delegates to pipelin, ndarray, dataset_creation(), dataset.py — captures face images from webcam or video for a named person. Calle, _resize_saved_images(), _evaluate(), get_embeddings() (+3 more)

### Community 5 - "Attendance Management System"
Cohesion: 0.15
Nodes (12): Attendance Management System, 👤 Author, ⬇️ Download Pre-trained Model, ML Pipeline, Project Structure, Requirements, 📄 Research Reference, Setup (+4 more)

### Community 6 - "user_interface.py"
Cohesion: 0.23
Nodes (10): _add_loss_summaries(), Add summaries for losses.        Generates moving average for all losses and ass, train(), gotohome(), s_exit(), show(), show_create(), show_run() (+2 more)

## Knowledge Gaps
- **11 isolated node(s):** `What it does`, `ML Pipeline`, `Tech Stack`, `Project Structure`, `Setup` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Network` connect `Network` to `detect_face.py`?**
  _High betweenness centrality (0.190) - this node is a cross-community bridge._
- **Why does `train()` connect `user_interface.py` to `facenet.py`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **What connects `main.py — entry point for the attendance management system. Delegates to pipelin`, `dataset.py — captures face images from webcam or video for a named person. Calle`, `recognizer.py — real-time face recognition via webcam, video, or image batch. Dr` to the rest of the system?**
  _39 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `facenet.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07396870554765292 - nodes in this community are weakly interconnected._
- **Should `detect_face.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._