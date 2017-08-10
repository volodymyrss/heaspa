def test_rmf_write():

    import heaspa
    import numpy as np

    rmf=heaspa.RMF(
            np.array([1,2]),
            np.array([2,3]),
            np.array([1,2]),
            np.array([2,3]),
            np.array([[1,0],[0,1]]))

    rmf.write("test_rmf.fits")

def test_pha_write():

    import heaspa
    import numpy as np

    rmf=heaspa.PHA(
            np.array([1,2]),
            np.array([2,3]),
            1.
        )

    rmf.write("test_pha.fits")
