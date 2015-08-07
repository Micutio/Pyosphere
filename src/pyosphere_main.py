"""
Main module of the Flow and Pressure Demo.
Uses the Complex Automaton Base.
"""

from cab_core.cab_system import ComplexAutomaton

from pyo_core.ca.cells import PyoHexCell
from pyo_core.abm.agents import SuperAgent
from pyo_core.global_constants import GlobalConstants
from pyo_core.util.input_handling import InputHandler
from pyo_core.util.visualization import Visualizer

__author__ = 'Michael Wagner'


if __name__ == '__main__':
    
    # Creating all main assets.

    gc = GlobalConstants()
    pc = PyoHexCell(0, 0, 0, gc)
    pa = SuperAgent(0, 0, gc)
    ph = InputHandler(None)
    pv = Visualizer(gc, None)

    # Use assets to initialize simulation system.

    # simulation = ComplexAutomaton(gc, proto_cell=pc, proto_agent=pa, proto_handler=ph, proto_visualizer=pv)
    simulation = ComplexAutomaton(gc, proto_cell=pc, proto_agent=pa, proto_handler=ph, proto_visualizer=pv)

    # Run the simulation
    simulation.run_main_loop()

    # If need be, the simulation can be run in profiling mode too!
    # cProfile.run("simulation.run_main_loop()")