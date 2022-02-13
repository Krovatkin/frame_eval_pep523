import threading
import mymod

cdef PyObject* get_bytecode_while_frame_eval(PyThreadState *tstate, PyFrameObject *frame_obj, int exc):

    frame = <object> frame_obj
    print(f"Running function: {frame.f_code.co_name}")
    tstate.interp.eval_frame = _PyEval_EvalFrameDefault
    mymod.hello()
    tstate.interp.eval_frame = get_bytecode_while_frame_eval
    return _PyEval_EvalFrameDefault(tstate, frame_obj, exc)

def main():
    cdef PyThreadState *state = PyThreadState_Get()
    state.interp.eval_frame = get_bytecode_while_frame_eval

def stop_frame_eval():
    cdef PyThreadState *state = PyThreadState_Get()
    state.interp.eval_frame = _PyEval_EvalFrameDefault
