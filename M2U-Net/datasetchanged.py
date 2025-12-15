from pathlib import Path
from PIL import Image
import numpy as np
from torch.utils.data import Dataset
import torchvision.transforms.functional as VF

def get_file_lists(image_file_path):
    """
    Args:
        image_file_path
    returns:
        list of file names in path
    """
    file_paths = sorted(list(image_file_path.glob('*')))
    return file_paths

class RetinaDataset(Dataset):
        """
        Args: 
            image_file names: a list of image file names with path
            dataset: 'DRIVE' or 'CHASE_DB1'
        """
        def __init__(self, file_paths: list,dataset='DRIVE'):
            self.file_paths = file_paths
            self.dataset = dataset
            
            self.root_dir = file_paths[0].parents[1]  # e.g., data/DRIVE/training/
            self.manual_dir = self.root_dir / '1st_manual'
            self.mask_dir = self.root_dir / 'mask'

        def __len__(self):
            return len(self.file_paths)

        def __getitem__(self,idx):
            # pick a file
            #img_file_name = str(self.file_paths[idx]) # pick a file
            #img = Image.open(img_file_name)
            
             # Input image
            img_path = Path(self.file_paths[idx])
            img = Image.open(img_path).convert("RGB")

            # File name base (e.g., 21_training.tif → 21_training)
            base_name = img_path.stem.replace('_training', '')
            #base_name = img_path.stem.split('_')[0]

            # Ground truth vessel annotation (1st_manual)
            label_path = Path(self.manual_dir / f"{base_name}_manual1.gif")
            label = Image.open(label_path).convert("L")

            # Field-of-view mask
            mask_path = Path(self.mask_dir / f"{base_name}_training_mask.gif")
            #mask_path = Path(self.mask_dir / f"{base_name}_test_mask.gif")
            mask = Image.open(mask_path).convert("L")

            # Preprocess all (center crop to 544x544)
            if self.dataset == 'DRIVE':
                img = VF.center_crop(img, (544, 544))
                label = VF.center_crop(label, (544, 544))
                mask = VF.center_crop(mask, (544, 544))

            return {
                'image': VF.to_tensor(img),
                'label': VF.to_tensor(label),
                'mask': VF.to_tensor(mask)
            }