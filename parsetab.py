
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LTHANEQ MAIN OR PROGRAMA RETURN VOID WHILE WRITEprograma : ID ';' vars programaF mainmain : MAIN '(' ')' bloqueprogramaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque\n                | emptyfunctionAux : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' bloque condicionelsecondicionelse : ELSE bloque\n                        | emptywrite : WRITE '(' superexpresion ')' ';' while : WHILE '(' superexpresion ')' bloqueasignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' exp\n            | '-' exp\n            | emptytermino : factor terminopterminop : '*' termino\n                | '/' termino\n                | emptyfactor : constante\n                | lParen superexpresion rParen lParen : '(' rParen : ')' constante : id\n                | CTEF ctef\n                | CTEI cteictef : ctei : functionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '(' idpp ')'\n            | '[' superexpresion ']'\n            | emptyidpp : superexpresion idppp\n            | emptyidppp : ',' idpp\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,5,6,7,8,9,10,20,21,22,23,24,26,30,35,39,41,44,45,47,48,49,50,51,52,53,58,65,66,67,68,69,70,77,81,83,84,93,95,96,99,100,101,102,103,104,107,108,111,112,121,142,145,146,147,148,150,152,153,],[2,-65,16,-67,-71,-72,-73,29,-8,-9,-10,-82,16,-66,-82,43,59,-11,-27,59,-20,-15,-16,-17,-18,-19,59,-28,59,59,59,59,59,59,-53,59,59,-21,59,59,59,59,59,59,59,59,59,59,59,59,-29,59,-30,-82,-25,-26,-22,-24,-23,]),'$end':([1,17,34,44,],[0,-1,-2,-11,]),';':([2,15,16,25,27,31,59,71,72,73,74,75,76,78,79,80,82,85,88,94,97,98,105,106,109,110,113,115,116,122,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,144,],[3,24,-82,-68,-70,-69,-82,93,-82,-82,-82,-82,-51,-55,-58,-59,-74,-77,121,-31,-34,-35,-42,-43,-46,-47,-50,-56,-57,145,147,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-76,]),'INT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,93,121,145,146,147,148,150,152,153,],[8,-65,-67,21,8,-66,8,8,8,-11,-27,8,-20,-15,-16,-17,-18,-19,8,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'FLOAT':([3,5,7,14,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,93,121,145,146,147,148,150,152,153,],[9,-65,-67,22,9,-66,9,9,9,-11,-27,9,-20,-15,-16,-17,-18,-19,9,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'CHAR':([3,5,7,24,30,33,35,41,44,45,47,48,49,50,51,52,53,62,65,93,121,145,146,147,148,150,152,153,],[10,-65,-67,10,-66,10,10,10,-11,-27,10,-20,-15,-16,-17,-18,-19,10,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'FUNCTION':([3,4,5,7,12,13,24,30,44,86,],[-82,14,-65,-67,14,-6,-82,-66,-11,-5,]),'MAIN':([3,4,5,7,11,12,13,19,24,30,44,86,],[-82,-82,-65,-67,18,-82,-4,-3,-82,-66,-11,-5,]),'IF':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,93,121,145,146,147,148,150,152,153,],[-65,-67,-82,-66,-82,55,-11,-27,55,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'WRITE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,93,121,145,146,147,148,150,152,153,],[-65,-67,-82,-66,-82,56,-11,-27,56,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'WHILE':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,93,121,145,146,147,148,150,152,153,],[-65,-67,-82,-66,-82,57,-11,-27,57,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'RETURN':([5,7,24,30,35,41,44,45,47,48,49,50,51,52,53,65,93,121,145,146,147,148,150,152,153,],[-65,-67,-82,-66,-82,58,-11,-27,58,-20,-15,-16,-17,-18,-19,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'}':([5,7,24,30,35,40,41,44,45,46,47,48,49,50,51,52,53,64,65,93,121,145,146,147,148,150,152,153,],[-65,-67,-82,-66,-82,44,-82,-11,-27,-12,-82,-14,-15,-16,-17,-18,-19,-13,-28,-21,-29,-30,-82,-25,-26,-22,-24,-23,]),'VOID':([14,],[23,]),',':([16,43,59,72,73,74,75,76,78,79,80,82,85,94,97,98,105,106,109,110,113,115,116,118,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,144,],[26,62,-82,-82,-82,-82,-82,-51,-55,-58,-59,-74,-77,-31,-34,-35,-42,-43,-46,-47,-50,-56,-57,142,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-76,]),'(':([18,29,55,56,57,58,59,66,67,68,69,70,77,81,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[28,33,68,69,70,81,83,81,81,81,81,81,81,-53,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),')':([28,33,36,37,38,43,59,61,63,72,73,74,75,76,78,79,80,82,83,85,87,90,91,92,94,97,98,105,106,109,110,113,114,115,116,117,118,119,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,149,],[32,-82,42,-60,-61,-82,-82,-62,-64,-82,-82,-82,-82,-51,-55,-58,-59,-74,-82,-77,-63,123,124,125,-31,-34,-35,-42,-43,-46,-47,-50,139,-56,-57,140,-82,-79,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-78,-82,-81,-76,-80,]),'{':([32,42,60,123,125,151,],[35,-7,35,35,35,35,]),'ELSE':([44,146,],[-11,151,]),'=':([54,59,82,85,140,144,],[66,-82,-74,-77,-75,-76,]),'[':([54,59,82,85,140,144,],[67,84,-74,-77,-75,-76,]),'CTEF':([58,66,67,68,69,70,77,81,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[79,79,79,79,79,79,79,-53,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CTEI':([58,66,67,68,69,70,77,81,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[80,80,80,80,80,80,80,-53,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'*':([59,75,76,78,79,80,82,85,115,116,138,139,140,144,],[-82,111,-51,-55,-58,-59,-74,-77,-56,-57,-52,-54,-75,-76,]),'/':([59,75,76,78,79,80,82,85,115,116,138,139,140,144,],[-82,112,-51,-55,-58,-59,-74,-77,-56,-57,-52,-54,-75,-76,]),'+':([59,74,75,76,78,79,80,82,85,110,113,115,116,136,137,138,139,140,144,],[-82,107,-82,-51,-55,-58,-59,-74,-77,-47,-50,-56,-57,-48,-49,-52,-54,-75,-76,]),'-':([59,74,75,76,78,79,80,82,85,110,113,115,116,136,137,138,139,140,144,],[-82,108,-82,-51,-55,-58,-59,-74,-77,-47,-50,-56,-57,-48,-49,-52,-54,-75,-76,]),'<':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,99,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'>':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,100,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'EQUALS':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,101,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'DIFF':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,102,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'LTHANEQ':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,103,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'GTHANEQ':([59,73,74,75,76,78,79,80,82,85,106,109,110,113,115,116,134,135,136,137,138,139,140,144,],[-82,104,-82,-82,-51,-55,-58,-59,-74,-77,-43,-46,-47,-50,-56,-57,-44,-45,-48,-49,-52,-54,-75,-76,]),'AND':([59,72,73,74,75,76,78,79,80,82,85,98,105,106,109,110,113,115,116,128,129,130,131,132,133,134,135,136,137,138,139,140,144,],[-82,95,-82,-82,-82,-51,-55,-58,-59,-74,-77,-35,-42,-43,-46,-47,-50,-56,-57,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-76,]),'OR':([59,72,73,74,75,76,78,79,80,82,85,98,105,106,109,110,113,115,116,128,129,130,131,132,133,134,135,136,137,138,139,140,144,],[-82,96,-82,-82,-82,-51,-55,-58,-59,-74,-77,-35,-42,-43,-46,-47,-50,-56,-57,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-76,]),']':([59,72,73,74,75,76,78,79,80,82,85,89,94,97,98,105,106,109,110,113,115,116,120,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,144,],[-82,-82,-82,-82,-82,-51,-55,-58,-59,-74,-77,122,-31,-34,-35,-42,-43,-46,-47,-50,-56,-57,144,-32,-33,-36,-37,-38,-39,-40,-41,-44,-45,-48,-49,-52,-54,-75,-76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([3,35,41,47,],[4,41,45,45,]),'varsp':([3,24,35,41,47,],[5,30,5,5,5,]),'tipo':([3,24,33,35,41,47,62,],[6,6,39,6,6,6,39,]),'empty':([3,4,12,16,24,33,35,41,43,47,59,72,73,74,75,83,118,142,146,],[7,13,13,27,7,38,7,48,63,48,85,97,105,109,113,119,143,119,152,]),'programaF':([4,12,],[11,19,]),'function':([4,12,],[12,12,]),'varspp':([6,26,],[15,31,]),'main':([11,],[17,]),'tipoRetorno':([14,],[20,]),'varsppp':([16,],[25,]),'bloque':([32,60,123,125,151,],[34,86,146,148,153,]),'functionParam':([33,],[36,]),'parametro':([33,62,],[37,87,]),'cuerpo':([35,],[40,]),'estatutop':([41,47,],[46,64,]),'estatuto':([41,47,],[47,47,]),'asignacion':([41,47,],[49,49,]),'condicion':([41,47,],[50,50,]),'write':([41,47,],[51,51,]),'while':([41,47,],[52,52,]),'return':([41,47,],[53,53,]),'id':([41,47,58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[54,54,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'functionAux':([42,],[60,]),'parametrop':([43,],[61,]),'asignacionp':([54,],[65,]),'superexpresion':([58,66,67,68,69,70,77,83,84,95,96,142,],[71,88,89,90,91,92,114,118,120,126,127,118,]),'megaexpresion':([58,66,67,68,69,70,77,83,84,95,96,142,],[72,72,72,72,72,72,72,72,72,72,72,72,]),'exp':([58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,142,],[73,73,73,73,73,73,73,73,73,73,73,128,129,130,131,132,133,134,135,73,]),'termino':([58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,136,137,74,]),'factor':([58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'constante':([58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'lParen':([58,66,67,68,69,70,77,83,84,95,96,99,100,101,102,103,104,107,108,111,112,142,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'idp':([59,],[82,]),'superexpresionp':([72,],[94,]),'megaexpresionp':([73,],[98,]),'expp':([74,],[106,]),'terminop':([75,],[110,]),'ctef':([79,],[115,]),'ctei':([80,],[116,]),'idpp':([83,142,],[117,149,]),'rParen':([114,],[138,]),'idppp':([118,],[141,]),'condicionelse':([146,],[150,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ID ; vars programaF main','programa',5,'p_programa','parser.py',18),
  ('main -> MAIN ( ) bloque','main',4,'p_main','parser.py',21),
  ('programaF -> function programaF','programaF',2,'p_programaF','parser.py',24),
  ('programaF -> empty','programaF',1,'p_programaF','parser.py',25),
  ('function -> FUNCTION tipoRetorno ID ( functionParam ) functionAux bloque','function',8,'p_function','parser.py',28),
  ('function -> empty','function',1,'p_function','parser.py',29),
  ('functionAux -> <empty>','functionAux',0,'p_functionAux','parser.py',32),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',44),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',45),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',46),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',50),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',53),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',56),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',57),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',60),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',61),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',62),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',63),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',64),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',65),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',69),
  ('condicion -> IF ( superexpresion ) bloque condicionelse','condicion',6,'p_condicion','parser.py',72),
  ('condicionelse -> ELSE bloque','condicionelse',2,'p_condicionelse','parser.py',75),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',76),
  ('write -> WRITE ( superexpresion ) ;','write',5,'p_write','parser.py',79),
  ('while -> WHILE ( superexpresion ) bloque','while',5,'p_while','parser.py',93),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',96),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',97),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',100),
  ('asignacionp -> [ superexpresion ] ;','asignacionp',4,'p_asignacionp','parser.py',101),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',104),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',120),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',121),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',122),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',127),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',142),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',143),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',144),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',145),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',146),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',147),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',148),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',153),
  ('expp -> + exp','expp',2,'p_expp','parser.py',168),
  ('expp -> - exp','expp',2,'p_expp','parser.py',169),
  ('expp -> empty','expp',1,'p_expp','parser.py',170),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',175),
  ('terminop -> * termino','terminop',2,'p_terminop','parser.py',190),
  ('terminop -> / termino','terminop',2,'p_terminop','parser.py',191),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',192),
  ('factor -> constante','factor',1,'p_factor','parser.py',197),
  ('factor -> lParen superexpresion rParen','factor',3,'p_factor','parser.py',198),
  ('lParen -> (','lParen',1,'p_lParen','parser.py',201),
  ('rParen -> )','rParen',1,'p_rParen','parser.py',205),
  ('constante -> id','constante',1,'p_constante','parser.py',209),
  ('constante -> CTEF ctef','constante',2,'p_constante','parser.py',210),
  ('constante -> CTEI ctei','constante',2,'p_constante','parser.py',211),
  ('ctef -> <empty>','ctef',0,'p_ctef','parser.py',214),
  ('ctei -> <empty>','ctei',0,'p_ctei','parser.py',220),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',226),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',227),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',230),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',236),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',237),
  ('vars -> varsp','vars',1,'p_vars','parser.py',240),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',244),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',245),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',248),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',265),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',266),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',269),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',270),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',271),
  ('id -> ID idp','id',2,'p_id','parser.py',275),
  ('idp -> ( idpp )','idp',3,'p_idp','parser.py',278),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',279),
  ('idp -> empty','idp',1,'p_idp','parser.py',280),
  ('idpp -> superexpresion idppp','idpp',2,'p_idpp','parser.py',285),
  ('idpp -> empty','idpp',1,'p_idpp','parser.py',286),
  ('idppp -> , idpp','idppp',2,'p_idppp','parser.py',289),
  ('idppp -> empty','idppp',1,'p_idppp','parser.py',290),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',293),
]
