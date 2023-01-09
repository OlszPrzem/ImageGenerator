from queue import Queue
import datetime

import imageGenerator as ig


class MainProgram:

    def __init__(self) -> None:

        self.queue_A = Queue()
        self.queue_B = Queue()
        self.num_frames_to_generate = 100

        _now = datetime.datetime.now()
        self.base_name_saved_imgs = _now.strftime("%Y%m%d_%H%M%S")

        self.path_folder_to_save_img = ig.create_save_folder(
            name_folder_to_save_img="processed"
            )
    
        self.source = ig.Source((1024, 768, 3))

        self.producer = ig.Producer(
            self.source.get_data, 
            queue_A = self.queue_A, 
            )

        self.consumer = ig.Consumer(
            queue_A = self.queue_A,
            queue_B = self.queue_B
        )

    def main_loop(self):
        
        run_program = True
        num_actual_saved_img = 0

        self.producer.start()
        self.consumer.start()


        while run_program:

            if not self.queue_B.empty():
                frame = self.queue_B.get()

                name_img = self.generate_name(num_actual_saved_img)
                ig.save_img(
                    frame, 
                    path_folder_to_save_frame = self.path_folder_to_save_img,
                    file_name = name_img
                    )

                num_actual_saved_img +=1

                if num_actual_saved_img >= self.num_frames_to_generate:
                    run_program = False

        self.producer.stop()
        self.consumer.stop()

    def generate_name(self, num_actual_saved_img):
        return "{}_{}.png".format(
            self.base_name_saved_imgs, 
            num_actual_saved_img,
            )
        

if __name__ == "__main__":
    task = MainProgram()
    task.main_loop()