# https://cran.r-project.org/web/packages/sets/sets.pdf
library(sets)

# Universes of discourse
# Range of values that the fuzzy variables may take
unv_number_steps =  seq(from=1.0, to=40.0, by=1.0)
unv_acc_deviation = seq(from=0.0, to=4.0, by=0.1)
unv_time =          seq(from=0.0, to=60.0, by=1.0)
unv_adequacy =      seq(from=0.0, to=1.0, by=0.01)

# Set of variables
variables <- set(
    number_steps = fuzzy_partition(
      varnames=c(VL=0.0, L=10.0, M=20.0, H=30.0, VH=40.0),
      FUN=fuzzy_cone, radius=10, universe=unv_number_steps),
    
    acc_deviation = fuzzy_partition(
      varnames= c(VL=0.0, L=1.0, M=2.0, H=3.0, VH=4.0),
      sd=0.3, universe=unv_acc_deviation),
    
    time = fuzzy_partition(
      varnames= c(VL=0.0, L=15.0, M=30.0, H=45.0, VH=60.0),
      FUN=fuzzy_cone, radius=15, universe=unv_time),
    
    adequacy = fuzzy_partition(
      varnames=c(VL=0, L=0.25, M=0.5, H=0.75, VH=1.0),
      sd=0.08, universe=unv_adequacy)
  )

# Set of rules
rules <- set(
  fuzzy_rule(number_steps %is% VH && acc_deviation %is% VH && time %is% VH, 
             adequacy %is% VL),
  fuzzy_rule(number_steps %is% VL && acc_deviation %is% VL && time %is% VL, 
             adequacy %is% VL),
  fuzzy_rule(number_steps %is% L && acc_deviation %is% L && time %is% L, 
             adequacy %is% L),
  fuzzy_rule(number_steps %is% H && acc_deviation %is% H && time %is% H, 
             adequacy %is% H),
  fuzzy_rule(number_steps %is% M && acc_deviation %is% M && time %is% M, 
             adequacy %is% M),
  
  # IF the accumulated deviation is VH,
  # THEN the patient is not performing the routine properly. 
  fuzzy_rule(acc_deviation %is% VH, 
             adequacy %is% VL),
  
  # IF the values are VL in two input variables,
  # THEN the adecuaccy is VL
  fuzzy_rule(number_steps %is% VL && acc_deviation %is% VL, 
             adequacy %is% VL),
  fuzzy_rule(number_steps %is% VL && time %is% VL, 
             adequacy %is% VL),
  fuzzy_rule(acc_deviation %is% VL && time %is% VL, 
             adequacy %is% VL),
  
  # IF the values are L in two input variables,
  # THEN the adecuacy is L
  fuzzy_rule(number_steps %is% L && acc_deviation %is% L,
             adequacy %is% L),
  fuzzy_rule(number_steps %is% L && time %is% L, 
             adequacy %is% L),
  fuzzy_rule(acc_deviation %is% L && time %is% L,
             adequacy %is% L),
  
  # Other rules...
  fuzzy_rule(number_steps %is% M && acc_deviation %is% L, 
             adequacy %is% H),
  fuzzy_rule(time %is% H, 
             adequacy %is% M)
)

model <- fuzzy_system (variables, rules)
print(model)
plot(model)

example.1 <- fuzzy_inference(model, list(number_steps = 8,  
                                         time = 30, acc_deviation = 3.6))
gset_defuzzify(example.1, "centroid")
plot(example.1)

example.2 <- fuzzy_inference(model, list(number_steps = 23,  
                                         time = 50, acc_deviation = 1.5))
gset_defuzzify(example.2, "centroid")
plot(example.2)



