
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LTHANEQ MAIN OR PROGRAMA RETURN VOID WHILE WRITEprograma : ID ';' vars programaF mainmain : MAIN '(' ')' bloqueprogramaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' bloque\n                | emptytipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' bloque condicionelsecondicionelse : ELSE bloque\n                        | emptywrite : WRITE '(' superexpresion ')' ';' oper : '<'\n            | '>'\n            | EQUALS\n            | DIFF\n            | LTHANEQ\n            | GTHANEQwhile : WHILE '(' superexpresion ')' bloqueasignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' exp\n            | '-' exp\n            | emptytermino : factor terminopterminop : '*' exp\n                | '/' exp\n                | emptyfactor : constante\n                | '(' superexpresion ')' constante : id\n                | CTEF\n                | CTEIfunctionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '[' superexpresion ']'\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,5,6,7,8,9,10,20,21,22,23,24,26,30,35,39,41,44,45,47,48,49,50,51,52,53,58,65,66,67,68,69,70,77,82,90,92,93,96,97,98,99,100,101,104,105,108,109,113,132,133,134,135,136,138,139,],[2,-66,16,-68,-72,-73,-74,29,-7,-8,-9,-78,16,-67,-78,43,59,-10,-32,59,-19,-14,-15,-16,-17,-18,59,-33,59,59,59,59,59,59,59,-20,59,59,59,59,59,59,59,59,59,59,59,59,-34,-35,-78,-24,-31,-21,-23,-22,]),'$end':([1,17,34,44,],[0,-1,-2,-10,]),';':([2,15,16,25,27,31,59,71,72,73,74,75,76,78,79,80,81,83,85,91,94,95,102,103,106,107,110,114,116,118,119,120,121,122,123,124,125,126,127,128,129,130,131,],[3,24,-78,-69,-71,-70,-78,90,-78,-78,-78,-78,-56,-58,-59,-60,-75,-77,113,-36,-39,-40,-47,-48,-51,-52,-55,132,134,-37,-38,-41,-42,-43,-44,-45,-46,-49,-50,-53,-54,-57,-76,]),'INT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,90,113,132,133,134,135,136,138,139,],[8,-66,-68,21,8,-67,8,8,8,-10,-32,8,-19,-14,-15,-16,-17,-18,8,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'FLOAT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,90,113,132,133,134,135,136,138,139,],[9,-66,-68,22,9,-67,9,9,9,-10,-32,9,-19,-14,-15,-16,-17,-18,9,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'CHAR':([3,5,7,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,90,113,132,133,134,135,136,138,139,],[10,-66,-68,10,-67,10,10,10,-10,-32,10,-19,-14,-15,-16,-17,-18,10,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'FUNCTION':([3,4,5,7,12,13,24,30,44,60,],[-78,14,-66,-68,14,-6,-78,-67,-10,-5,]),'MAIN':([3,4,5,7,11,12,13,19,24,30,44,60,],[-78,-78,-66,-68,18,-78,-4,-3,-78,-67,-10,-5,]),'IF':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,90,113,132,133,134,135,136,138,139,],[-66,-68,-78,-67,-78,55,-10,-32,55,-19,-14,-15,-16,-17,-18,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'WRITE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,90,113,132,133,134,135,136,138,139,],[-66,-68,-78,-67,-78,56,-10,-32,56,-19,-14,-15,-16,-17,-18,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'WHILE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,90,113,132,133,134,135,136,138,139,],[-66,-68,-78,-67,-78,57,-10,-32,57,-19,-14,-15,-16,-17,-18,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'RETURN':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,90,113,132,133,134,135,136,138,139,],[-66,-68,-78,-67,-78,58,-10,-32,58,-19,-14,-15,-16,-17,-18,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'}':([5,7,24,30,35,40,41,44,45,46,47,48,49,50,51,52,53,64,65,90,113,132,133,134,135,136,138,139,],[-66,-68,-78,-67,-78,44,-78,-10,-32,-11,-78,-13,-14,-15,-16,-17,-18,-12,-33,-20,-34,-35,-78,-24,-31,-21,-23,-22,]),'VOID':([14,],[23,]),',':([16,43,],[26,62,]),'(':([18,29,55,56,57,58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[28,33,68,69,70,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),')':([28,33,36,37,38,43,59,61,63,72,73,74,75,76,78,79,80,81,83,84,87,88,89,91,94,95,102,103,106,107,110,111,118,119,120,121,122,123,124,125,126,127,128,129,130,131,],[32,-78,42,-61,-62,-78,-78,-63,-65,-78,-78,-78,-78,-56,-58,-59,-60,-75,-77,-64,115,116,117,-36,-39,-40,-47,-48,-51,-52,-55,130,-37,-38,-41,-42,-43,-44,-45,-46,-49,-50,-53,-54,-57,-76,]),'{':([32,42,115,117,137,],[35,35,35,35,35,]),'ELSE':([44,133,],[-10,137,]),'=':([54,59,81,83,131,],[66,-78,-75,-77,-76,]),'[':([54,59,81,83,131,],[67,82,-75,-77,-76,]),'CTEF':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CTEI':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'*':([59,75,76,78,79,80,81,83,130,131,],[-78,108,-56,-58,-59,-60,-75,-77,-57,-76,]),'/':([59,75,76,78,79,80,81,83,130,131,],[-78,109,-56,-58,-59,-60,-75,-77,-57,-76,]),'+':([59,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,104,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'-':([59,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,105,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'<':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,96,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'>':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,97,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'EQUALS':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,98,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'DIFF':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,99,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'LTHANEQ':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,100,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'GTHANEQ':([59,73,74,75,76,78,79,80,81,83,103,106,107,110,126,127,128,129,130,131,],[-78,101,-78,-78,-56,-58,-59,-60,-75,-77,-48,-51,-52,-55,-49,-50,-53,-54,-57,-76,]),'AND':([59,72,73,74,75,76,78,79,80,81,83,95,102,103,106,107,110,120,121,122,123,124,125,126,127,128,129,130,131,],[-78,92,-78,-78,-78,-56,-58,-59,-60,-75,-77,-40,-47,-48,-51,-52,-55,-41,-42,-43,-44,-45,-46,-49,-50,-53,-54,-57,-76,]),'OR':([59,72,73,74,75,76,78,79,80,81,83,95,102,103,106,107,110,120,121,122,123,124,125,126,127,128,129,130,131,],[-78,93,-78,-78,-78,-56,-58,-59,-60,-75,-77,-40,-47,-48,-51,-52,-55,-41,-42,-43,-44,-45,-46,-49,-50,-53,-54,-57,-76,]),']':([59,72,73,74,75,76,78,79,80,81,83,86,91,94,95,102,103,106,107,110,112,118,119,120,121,122,123,124,125,126,127,128,129,130,131,],[-78,-78,-78,-78,-78,-56,-58,-59,-60,-75,-77,114,-36,-39,-40,-47,-48,-51,-52,-55,131,-37,-38,-41,-42,-43,-44,-45,-46,-49,-50,-53,-54,-57,-76,]),}
=======
_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LTHANEQ MAIN OR PROGRAMA RETURN VOID WHILE WRITEprograma : ID ';' vars programaF mainmain : MAIN '(' ')' bloqueprogramaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque\n                | emptyfunctionAux : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' bloque condicionelsecondicionelse : ELSE bloque\n                        | emptywrite : WRITE '(' superexpresion ')' ';' while : WHILE '(' superexpresion ')' bloqueasignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' exp\n            | '-' exp\n            | emptytermino : factor terminopterminop : '*' exp\n                | '/' exp\n                | emptyfactor : constante\n                | '(' superexpresion ')' constante : id\n                | CTEF\n                | CTEIfunctionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '[' superexpresion ']'\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,5,6,7,8,9,10,20,21,22,23,24,26,30,35,39,41,44,45,47,48,49,50,51,52,53,58,65,66,67,68,69,70,77,82,91,93,94,97,98,99,100,101,102,105,106,109,110,114,133,134,135,136,137,139,140,],[2,-61,16,-63,-67,-68,-69,29,-8,-9,-10,-73,16,-62,-73,43,59,-11,-27,59,-20,-15,-16,-17,-18,-19,59,-28,59,59,59,59,59,59,59,-21,59,59,59,59,59,59,59,59,59,59,59,59,-29,-30,-73,-25,-26,-22,-24,-23,]),'$end':([1,17,34,44,],[0,-1,-2,-11,]),';':([2,15,16,25,27,31,59,71,72,73,74,75,76,78,79,80,81,83,86,92,95,96,103,104,107,108,111,115,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[3,24,-73,-64,-66,-65,-73,91,-73,-73,-73,-73,-51,-53,-54,-55,-70,-72,114,-31,-34,-35,-42,-43,-46,-47,-50,133,135,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-71,]),'INT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,91,114,133,134,135,136,137,139,140,],[8,-61,-63,21,8,-62,8,8,8,-11,-27,8,-20,-15,-16,-17,-18,-19,8,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'FLOAT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,91,114,133,134,135,136,137,139,140,],[9,-61,-63,22,9,-62,9,9,9,-11,-27,9,-20,-15,-16,-17,-18,-19,9,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'CHAR':([3,5,7,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,91,114,133,134,135,136,137,139,140,],[10,-61,-63,10,-62,10,10,10,-11,-27,10,-20,-15,-16,-17,-18,-19,10,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'FUNCTION':([3,4,5,7,12,13,24,30,44,84,],[-73,14,-61,-63,14,-6,-73,-62,-11,-5,]),'MAIN':([3,4,5,7,11,12,13,19,24,30,44,84,],[-73,-73,-61,-63,18,-73,-4,-3,-73,-62,-11,-5,]),'IF':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,91,114,133,134,135,136,137,139,140,],[-61,-63,-73,-62,-73,55,-11,-27,55,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'WRITE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,91,114,133,134,135,136,137,139,140,],[-61,-63,-73,-62,-73,56,-11,-27,56,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'WHILE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,91,114,133,134,135,136,137,139,140,],[-61,-63,-73,-62,-73,57,-11,-27,57,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'RETURN':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,91,114,133,134,135,136,137,139,140,],[-61,-63,-73,-62,-73,58,-11,-27,58,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'}':([5,7,24,30,35,40,41,44,45,46,47,48,49,50,51,52,53,64,65,91,114,133,134,135,136,137,139,140,],[-61,-63,-73,-62,-73,44,-73,-11,-27,-12,-73,-14,-15,-16,-17,-18,-19,-13,-28,-21,-29,-30,-73,-25,-26,-22,-24,-23,]),'VOID':([14,],[23,]),',':([16,43,],[26,62,]),'(':([18,29,55,56,57,58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[28,33,68,69,70,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),')':([28,33,36,37,38,43,59,61,63,72,73,74,75,76,78,79,80,81,83,85,88,89,90,92,95,96,103,104,107,108,111,112,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[32,-73,42,-56,-57,-73,-73,-58,-60,-73,-73,-73,-73,-51,-53,-54,-55,-70,-72,-59,116,117,118,-31,-34,-35,-42,-43,-46,-47,-50,131,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-71,]),'{':([32,42,60,116,118,138,],[35,-7,35,35,35,35,]),'ELSE':([44,134,],[-11,138,]),'=':([54,59,81,83,132,],[66,-73,-70,-72,-71,]),'[':([54,59,81,83,132,],[67,82,-70,-72,-71,]),'CTEF':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CTEI':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'*':([59,75,76,78,79,80,81,83,131,132,],[-73,109,-51,-53,-54,-55,-70,-72,-52,-71,]),'/':([59,75,76,78,79,80,81,83,131,132,],[-73,110,-51,-53,-54,-55,-70,-72,-52,-71,]),'+':([59,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,105,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'-':([59,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,106,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'<':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,97,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'>':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,98,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'EQUALS':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,99,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'DIFF':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,100,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'LTHANEQ':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,101,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'GTHANEQ':([59,73,74,75,76,78,79,80,81,83,104,107,108,111,127,128,129,130,131,132,],[-73,102,-73,-73,-51,-53,-54,-55,-70,-72,-43,-46,-47,-50,-44,-45,-48,-49,-52,-71,]),'AND':([59,72,73,74,75,76,78,79,80,81,83,96,103,104,107,108,111,121,122,123,124,125,126,127,128,129,130,131,132,],[-73,93,-73,-73,-73,-51,-53,-54,-55,-70,-72,-35,-42,-43,-46,-47,-50,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-71,]),'OR':([59,72,73,74,75,76,78,79,80,81,83,96,103,104,107,108,111,121,122,123,124,125,126,127,128,129,130,131,132,],[-73,94,-73,-73,-73,-51,-53,-54,-55,-70,-72,-35,-42,-43,-46,-47,-50,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-71,]),']':([59,72,73,74,75,76,78,79,80,81,83,87,92,95,96,103,104,107,108,111,113,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[-73,-73,-73,-73,-73,-51,-53,-54,-55,-70,-72,115,-31,-34,-35,-42,-43,-46,-47,-50,132,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-71,]),}
>>>>>>> DirectorioFunciones

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

<<<<<<< HEAD
_lr_goto_items = {'programa':([0,],[1,]),'vars':([3,35,41,47,],[4,41,45,45,]),'varsp':([3,24,35,41,47,],[5,30,5,5,5,]),'tipo':([3,24,33,35,41,47,62,],[6,6,39,6,6,6,39,]),'empty':([3,4,12,16,24,33,35,41,43,47,59,72,73,74,75,133,],[7,13,13,27,7,38,7,48,63,48,83,94,102,106,110,138,]),'programaF':([4,12,],[11,19,]),'function':([4,12,],[12,12,]),'varspp':([6,26,],[15,31,]),'main':([11,],[17,]),'tipoRetorno':([14,],[20,]),'varsppp':([16,],[25,]),'bloque':([32,42,115,117,137,],[34,60,133,135,139,]),'functionParam':([33,],[36,]),'parametro':([33,62,],[37,84,]),'cuerpo':([35,],[40,]),'estatutop':([41,47,],[46,64,]),'estatuto':([41,47,],[47,47,]),'asignacion':([41,47,],[49,49,]),'condicion':([41,47,],[50,50,]),'write':([41,47,],[51,51,]),'while':([41,47,],[52,52,]),'return':([41,47,],[53,53,]),'id':([41,47,58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[54,54,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'parametrop':([43,],[61,]),'asignacionp':([54,],[65,]),'superexpresion':([58,66,67,68,69,70,77,82,92,93,],[71,85,86,87,88,89,111,112,118,119,]),'megaexpresion':([58,66,67,68,69,70,77,82,92,93,],[72,72,72,72,72,72,72,72,72,72,]),'exp':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[73,73,73,73,73,73,73,73,73,73,120,121,122,123,124,125,126,127,128,129,]),'termino':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'factor':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'constante':([58,66,67,68,69,70,77,82,92,93,96,97,98,99,100,101,104,105,108,109,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'idp':([59,],[81,]),'superexpresionp':([72,],[91,]),'megaexpresionp':([73,],[95,]),'expp':([74,],[103,]),'terminop':([75,],[107,]),'condicionelse':([133,],[136,]),}
=======
_lr_goto_items = {'programa':([0,],[1,]),'vars':([3,35,41,47,],[4,41,45,45,]),'varsp':([3,24,35,41,47,],[5,30,5,5,5,]),'tipo':([3,24,33,35,41,47,62,],[6,6,39,6,6,6,39,]),'empty':([3,4,12,16,24,33,35,41,43,47,59,72,73,74,75,134,],[7,13,13,27,7,38,7,48,63,48,83,95,103,107,111,139,]),'programaF':([4,12,],[11,19,]),'function':([4,12,],[12,12,]),'varspp':([6,26,],[15,31,]),'main':([11,],[17,]),'tipoRetorno':([14,],[20,]),'varsppp':([16,],[25,]),'bloque':([32,60,116,118,138,],[34,84,134,136,140,]),'functionParam':([33,],[36,]),'parametro':([33,62,],[37,85,]),'cuerpo':([35,],[40,]),'estatutop':([41,47,],[46,64,]),'estatuto':([41,47,],[47,47,]),'asignacion':([41,47,],[49,49,]),'condicion':([41,47,],[50,50,]),'write':([41,47,],[51,51,]),'while':([41,47,],[52,52,]),'return':([41,47,],[53,53,]),'id':([41,47,58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[54,54,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'functionAux':([42,],[60,]),'parametrop':([43,],[61,]),'asignacionp':([54,],[65,]),'superexpresion':([58,66,67,68,69,70,77,82,93,94,],[71,86,87,88,89,90,112,113,119,120,]),'megaexpresion':([58,66,67,68,69,70,77,82,93,94,],[72,72,72,72,72,72,72,72,72,72,]),'exp':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[73,73,73,73,73,73,73,73,73,73,121,122,123,124,125,126,127,128,129,130,]),'termino':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'factor':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'constante':([58,66,67,68,69,70,77,82,93,94,97,98,99,100,101,102,105,106,109,110,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'idp':([59,],[81,]),'superexpresionp':([72,],[92,]),'megaexpresionp':([73,],[96,]),'expp':([74,],[104,]),'terminop':([75,],[108,]),'condicionelse':([134,],[137,]),}
>>>>>>> DirectorioFunciones

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ID ; vars programaF main','programa',5,'p_programa','parser.py',14),
  ('main -> MAIN ( ) bloque','main',4,'p_main','parser.py',17),
  ('programaF -> function programaF','programaF',2,'p_programaF','parser.py',20),
  ('programaF -> empty','programaF',1,'p_programaF','parser.py',21),
<<<<<<< HEAD
  ('function -> FUNCTION tipoRetorno ID ( functionParam ) bloque','function',7,'p_function','parser.py',24),
  ('function -> empty','function',1,'p_function','parser.py',25),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',28),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',29),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',30),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',35),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',38),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',41),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',42),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',45),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',46),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',47),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',48),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',49),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',50),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',54),
  ('condicion -> IF ( superexpresion ) bloque condicionelse','condicion',6,'p_condicion','parser.py',57),
  ('condicionelse -> ELSE bloque','condicionelse',2,'p_condicionelse','parser.py',60),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',61),
  ('write -> WRITE ( superexpresion ) ;','write',5,'p_write','parser.py',64),
  ('oper -> <','oper',1,'p_oper','parser.py',70),
  ('oper -> >','oper',1,'p_oper','parser.py',71),
  ('oper -> EQUALS','oper',1,'p_oper','parser.py',72),
  ('oper -> DIFF','oper',1,'p_oper','parser.py',73),
  ('oper -> LTHANEQ','oper',1,'p_oper','parser.py',74),
  ('oper -> GTHANEQ','oper',1,'p_oper','parser.py',75),
  ('while -> WHILE ( superexpresion ) bloque','while',5,'p_while','parser.py',78),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',81),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',82),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',85),
  ('asignacionp -> [ superexpresion ] ;','asignacionp',4,'p_asignacionp','parser.py',86),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',89),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',92),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',93),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',94),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',97),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',100),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',101),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',102),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',103),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',104),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',105),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',106),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',109),
  ('expp -> + exp','expp',2,'p_expp','parser.py',112),
  ('expp -> - exp','expp',2,'p_expp','parser.py',113),
  ('expp -> empty','expp',1,'p_expp','parser.py',114),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',117),
  ('terminop -> * exp','terminop',2,'p_terminop','parser.py',120),
  ('terminop -> / exp','terminop',2,'p_terminop','parser.py',121),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',122),
  ('factor -> constante','factor',1,'p_factor','parser.py',125),
  ('factor -> ( superexpresion )','factor',3,'p_factor','parser.py',126),
  ('constante -> id','constante',1,'p_constante','parser.py',129),
  ('constante -> CTEF','constante',1,'p_constante','parser.py',130),
  ('constante -> CTEI','constante',1,'p_constante','parser.py',131),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',134),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',135),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',138),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',145),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',146),
  ('vars -> varsp','vars',1,'p_vars','parser.py',149),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',154),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',155),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',158),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',176),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',177),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',180),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',181),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',182),
  ('id -> ID idp','id',2,'p_id','parser.py',187),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',190),
  ('idp -> empty','idp',1,'p_idp','parser.py',191),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',194),
=======
  ('function -> FUNCTION tipoRetorno ID ( functionParam ) functionAux bloque','function',8,'p_function','parser.py',24),
  ('function -> empty','function',1,'p_function','parser.py',25),
  ('functionAux -> <empty>','functionAux',0,'p_functionAux','parser.py',28),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',42),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',43),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',44),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',49),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',52),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',55),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',56),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',59),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',60),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',61),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',62),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',63),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',64),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',68),
  ('condicion -> IF ( superexpresion ) bloque condicionelse','condicion',6,'p_condicion','parser.py',71),
  ('condicionelse -> ELSE bloque','condicionelse',2,'p_condicionelse','parser.py',74),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',75),
  ('write -> WRITE ( superexpresion ) ;','write',5,'p_write','parser.py',78),
  ('while -> WHILE ( superexpresion ) bloque','while',5,'p_while','parser.py',92),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',95),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',96),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',99),
  ('asignacionp -> [ superexpresion ] ;','asignacionp',4,'p_asignacionp','parser.py',100),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',103),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',106),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',107),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',108),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',111),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',114),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',115),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',116),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',117),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',118),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',119),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',120),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',123),
  ('expp -> + exp','expp',2,'p_expp','parser.py',126),
  ('expp -> - exp','expp',2,'p_expp','parser.py',127),
  ('expp -> empty','expp',1,'p_expp','parser.py',128),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',131),
  ('terminop -> * exp','terminop',2,'p_terminop','parser.py',134),
  ('terminop -> / exp','terminop',2,'p_terminop','parser.py',135),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',136),
  ('factor -> constante','factor',1,'p_factor','parser.py',139),
  ('factor -> ( superexpresion )','factor',3,'p_factor','parser.py',140),
  ('constante -> id','constante',1,'p_constante','parser.py',143),
  ('constante -> CTEF','constante',1,'p_constante','parser.py',144),
  ('constante -> CTEI','constante',1,'p_constante','parser.py',145),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',148),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',149),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',152),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',159),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',160),
  ('vars -> varsp','vars',1,'p_vars','parser.py',163),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',168),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',169),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',172),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',190),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',191),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',194),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',195),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',196),
  ('id -> ID idp','id',2,'p_id','parser.py',201),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',204),
  ('idp -> empty','idp',1,'p_idp','parser.py',205),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',208),
>>>>>>> DirectorioFunciones
]
