rho_n = 6.338E28

[Mesh]
  type = GeneratedMesh
  dim = 1
  nx = 1000
  xmax = 1e-3
[]

[Variables]
  [mobile][]
  [trapped][]
[]

[Functions]
  [temperature]
    type = ParsedFunction
    expression = '1000'
  []

  [diffusivity_func]
    type = ParsedFunction
    symbol_names = 'T'
    symbol_values = 'temperature'
    expression = '1.9e-7*exp(-0.2/8.617e-05/T)'
  []

  [trapping_rate]
    type = ParsedFunction
    symbol_names = 'T'
    symbol_values = 'temperature'
    expression = '2.62e-17*exp(-0.2/8.617e-05/T)'
  []

  [max_time_step_size_func]
    type = ParsedFunction
    expression = 'if(0.25e6 < t < 0.4e6, 1e3, 100000)'
  []
[]

[Kernels]
  [diff]
    type = ADMatDiffusion
    variable = mobile
    diffusivity = diffusivity_material
    block = 0
  []
  [./time]
    type = TimeDerivative
    variable = mobile
  [../]
[]

[Materials]
  [diff_solu]
    type = ADGenericFunctionMaterial
    prop_names = 'diffusivity_material'
    prop_values = 'diffusivity_func'
    outputs = all
  []

  [converter_to_regular]
    type = MaterialADConverter
    ad_props_in = 'diffusivity_material'
    reg_props_out = 'diffusivity_material_nonAD'
  []

[]

[NodalKernels]
  [time]
    type = TimeDerivativeNodalKernel
    variable = trapped
  []
  [trapping]
    type = TrappingNodalKernel
    variable = trapped
    alpha_t = ${fparse 2.57e-18 * rho_n}  # alpha_t has to be double and cannot be T dependent
    N = ${fparse rho_n}
    Ct0 = 1E-3
    mobile = 'mobile'
  []
  [release]
    type = ReleasingNodalKernel
    alpha_r = 1e13
    temp = 1000
    trapping_energy = 2.5
    variable = trapped
  []
[]

[BCs]
  [left]
    type = DirichletBC
    variable = mobile
    value = 5.3e+21
    boundary = left
  []
  [right]
    type = DirichletBC
    variable = mobile
    value = 0
    boundary = right
  []
[]

[Postprocessors]
  [outflux]
    type = SideDiffusiveFluxAverage
    boundary = right
    diffusivity = diffusivity_material_nonAD
    variable = mobile
  []
[]

[Executioner]
  type = Transient
  end_time = 1E6
  dt = 0.1
  solve_type = NEWTON
  line_search = 'none'
  verbose = true
  nl_abs_tol = 1e10
  nl_rel_tol = 1e-10
[]

[Outputs]
  exodus = true
  csv = true
[]
