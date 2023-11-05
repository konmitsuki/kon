def create_video_from_images(image_directory, output_video_path, frame_rate=30, frame_size=(640, 480)):
    images = [f for f in os.listdir(image_directory) if f.endswith('.bmp')]

    # サポートされるビデオコーデックとして、'XVID' を指定します（Windows用）
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, frame_size)

    for image in images:
        image_path = os.path.join(image_directory, image)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_directory = 'images/'  # 画像が格納されているディレクトリ
    output_video_path = 'output_video.avi'  # 作成されるビデオの名前

    create_video_from_images(input_image_directory, output_video_path)