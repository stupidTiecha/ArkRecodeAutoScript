from cnocr import CnOcr
from cnocr.cn_ocr import *


class ocr(CnOcr):
    def __init__(self,
                 rec_model_name: str = 'densenet_lite_136-fc',
                 *,
                 det_model_name: str = 'ch_PP-OCRv3_det',
                 cand_alphabet: Optional[Union[Collection, str]] = None,
                 context: str = 'cpu',  # ['cpu', 'gpu', 'cuda']
                 rec_model_fp: Optional[str] = None,
                 rec_model_backend: str = 'onnx',  # ['pytorch', 'onnx']
                 rec_vocab_fp: Optional[Union[str, Path]] = None,
                 rec_more_configs: Optional[Dict[str, Any]] = None,
                 rec_root: Union[str, Path] = data_dir(),
                 det_model_fp: Optional[str] = None,
                 det_model_backend: str = 'onnx',  # ['pytorch', 'onnx']
                 det_more_configs: Optional[Dict[str, Any]] = None,
                 det_root: Union[str, Path] = det_data_dir(),
                 **kwargs, ):
        super().__init__(**kwargs)



if __name__ == '__main__':
    img = '../../assets/GAME_VERSION.png'
    cnocr = CnOcr()
    out = cnocr.ocr(img,rec_model_name='densenet_lite_136-fc', det_model_name='naive_det', cand_alphabet='0123456789')
    print(out)
