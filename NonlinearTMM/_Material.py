import numpy as np
from  NonlinearTMM import _SecondOrderNLTMMCython  # @UnresolvedImport

__all__ = ["Material"]

class Material(_SecondOrderNLTMMCython.Material):# @UndefinedVariable
    @staticmethod
    def Static(n):
        wls = np.array([-1.0, 1.0])
        ns = np.array([n, n], dtype = complex)
        res = Material(wls, ns)
        return res
    
    @staticmethod
    def FromLabPy(materialLabPy):
        if materialLabPy.materialFile == "Static":
            wls = np.array([-1.0, 1.0])
            n = materialLabPy.n + 1.0j * (materialLabPy.k + materialLabPy.kAdditional)
            ns = np.array([n, n], dtype = complex)
        elif materialLabPy.isFormula:
            wls = np.ascontiguousarray(np.linspace(materialLabPy.wlRange[0], materialLabPy.wlRange[1], 500))
            ns = np.ascontiguousarray(materialLabPy(wls))
        else:
            wls = np.ascontiguousarray(materialLabPy.wlExp)
            if materialLabPy.kExp is None:
                ns = np.ascontiguousarray(materialLabPy.nExp, dtype = complex)
            else:
                ns = np.ascontiguousarray(materialLabPy.nExp + 1.0j * materialLabPy.kExp)
            ns += 1.0j * materialLabPy.kAdditional
        res = Material(wls, ns)
        res._materialLabPy = materialLabPy
        return res
   
if __name__ == "__main__":
    pass