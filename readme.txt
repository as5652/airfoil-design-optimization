Airfoil Optimization with XFOIL, Genetic Algorithms, and Reinforcement Learning

This project provides a complete pipeline for airfoil shape optimization using Soft Actor-Critic (SAC), Deep Deterministic Policy Gradient (DDPG), and a Genetic Algorithm (GA). Airfoils are defined using Bézier curves, automatically converted into XFOIL-compatible .dat files, evaluated aerodynamically, and refined through optimization. The framework integrates Gymnasium, Stable-Baselines3, XFOIL, and custom geometry-generation tools.

------------------------------------------------------------
1. Genetic Algorithms (GA)

Purpose:
Explore the airfoil design space through evolutionary optimization.

Structure:
A GA would operate directly on the 8-point Bézier geometry vector, using the same evaluation function as the RL environment.

Records Maintained (typical GA fields):
- Best-performing geometry each generation
- Fitness values (L/D) for all candidates
- Convergence curve
- Mutation/crossover histories

Objective:
- Maximize L/D under the same aerodynamic and geometric constraints as RL.

Variables Optimized:
- Upper-curve control points: [yu1, yu2, yu3, yu4]
- Lower-curve control points: [yl1, yl2, yl3, yl4]

------------------------------------------------------------
2. Reinforcement Learning (RL)

Purpose:
Train an RL agent to iteratively adjust Bézier control points to produce airfoils with improved aerodynamic efficiency.

Implemented Algorithms:
- Soft Actor-Critic (SAC)
- Deep Deterministic Policy Gradient (DDPG)

Environment:
- custom_env.py defines XFOILEnv, a continuous-action environment wrapping XFOIL.

Records Maintained:
- Airfoil geometry history (Bézier curves)
- L/D performance history
- Sequence of states and actions
- Saved .dat airfoil files

Objective:
- Maximize lift-to-drag ratio (L/D) averaged across angles of attack.

Constraints:
- No self-intersecting geometry
- Minimum thickness constraints per control-point pair
- Leading/trailing edge fixed at (0,0) and (1,0)
- Bézier point movement limited to ±0.15
- Airfoil shape must remain within observation bounds

Variables:
- 8 control-point vertical displacements (state)
- 8 continuous action values (Δy adjustments)
- Reward = mean(L/D) from XFOIL
- Discount factor, learning rate, network size (via SAC/DDPG hyperparameters)

------------------------------------------------------------
3. XFOIL Automation

Purpose:
Automate generation, simulation, and extraction of aerodynamic performance.

Functions Used:
- simulate_airfoil(foil_name)
- bezier_curve(…) (creates .dat file for XFOIL)

Inputs:
- Bézier-based airfoil .dat file
- Reynolds number (default: 1,000,000)
- Angle-of-attack sweep (default: 5° to 7°)
- Maximum iteration count (default: 250)

Outputs:
- polar_file.txt containing:
  - Lift coefficient (CL)
  - Drag coefficient (CD)
  - L/D ratio
- Returned L/D array for reward calculation

Features:
- Automatic .dat file creation
- Automatic generation of XFOIL input script
- XFOIL is invoked via subprocess.call()
- Robust handling when XFOIL fails (returns L/D = 0)

------------------------------------------------------------
4. Bezier Curve Airfoil Generation

Purpose:
Generate smooth, continuous airfoils suitable for aerodynamic simulation.

Functions:
- bezier_curve(foil_name, yu, yl)
- Builds full upper and lower surfaces
- Computes 100 Bézier-sampled points
- Writes XFOIL-compatible airfoil geometry file
- Returns full x/y distributions for plotting

Inputs:
- yu: Upper surface control-point y-values
- yl: Lower surface control-point y-values
- 100 sampling points distributed via linspace

Outputs:
- (Pxu, Pyu) upper surface points
- (Pxl, Pyl) lower surface points
- <foil_name>.dat written to workspace

------------------------------------------------------------
5. Visualization

Purpose:
Provide graphical insight into geometry evolution and aerodynamic performance.

Functions:
- plot_airfoil(env)
- Loads all generated Airfoil_*.dat files
- Animates the shape evolution step-by-step
- Plots Bézier points and actual airfoil surface
- plot_performance(env, window=50)
- Moving-average L/D plot
- Shows learning stability and convergence during RL training

Inputs:
- Geometry logs from XFOILEnv
- Performance logs (L/D values)

Outputs:
- Training animations
- Performance trend plots

------------------------------------------------------------
6. Installation

1. Clone the repository:
   git clone <repository_url>
   cd <repository_folder>

2. Install required Python packages:
   pip install -r requirements.txt

3. Ensure XFOIL is installed and accessible from your system path.

------------------------------------------------------------
7. Usage

1. Run SAC optimization:
   python sac_main.py

2. Run DDPG optimization:
   python ddpg_main.py

3. Run GA optimization:
   python ga_main.py

------------------------------------------------------------
Notes

- All airfoil designs follow geometric constraints to ensure realistic shapes.
- Both GA and RL approaches aim to maximize L/D ratio but use different optimization strategies.

------------------------------------------------------------
References

- XFOIL Airfoil Analysis Tool: http://web.mit.edu/drela/Public/web/xfoil/
- Genetic Algorithms: https://en.wikipedia.org/wiki/Genetic_algorithm
- Reinforcement Learning: https://en.wikipedia.org/wiki/Reinforcement_learning
- https://github.com/JARC99/xfoil-runner
