
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LTHANEQ MAIN OR PROGRAMA RETURN VOID WHILE WRITEprograma : ID ';' vars programaF mainmain : MAIN '(' ')' bloqueprogramaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID functionAux '(' functionParam ')' bloque\n                | emptyfunctionAux : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' bloque condicionelsecondicionelse : ELSE bloque\n                        | emptywrite : WRITE '(' superexpresion ')' ';' oper : '<'\n            | '>'\n            | EQUALS\n            | DIFF\n            | LTHANEQ\n            | GTHANEQwhile : WHILE '(' superexpresion ')' bloqueasignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' exp\n            | '-' exp\n            | emptytermino : factor terminopterminop : '*' exp\n                | '/' exp\n                | emptyfactor : constante\n                | '(' superexpresion ')' constante : id\n                | CTEF\n                | CTEIfunctionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '[' superexpresion ']'\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,5,6,7,8,9,10,20,21,22,23,24,26,30,35,38,42,43,44,46,47,48,49,50,51,52,57,62,63,64,65,66,67,74,79,90,92,93,96,97,98,99,100,101,104,105,108,109,114,133,134,135,136,137,139,140,],[2,-67,16,-69,-73,-74,-75,29,-8,-9,-10,-79,16,-68,-79,58,60,-11,-33,58,-20,-15,-16,-17,-18,-19,58,-34,58,58,58,58,58,58,58,-21,58,58,58,58,58,58,58,58,58,58,58,58,-35,-36,-79,-25,-32,-22,-24,-23,]),'$end':([1,17,34,43,],[0,-1,-2,-11,]),';':([2,15,16,25,27,31,58,68,69,70,71,72,73,75,76,77,78,80,85,91,94,95,102,103,106,107,110,115,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[3,24,-79,-70,-72,-71,-79,90,-79,-79,-79,-79,-57,-59,-60,-61,-76,-78,114,-37,-40,-41,-48,-49,-52,-53,-56,133,135,-38,-39,-42,-43,-44,-45,-46,-47,-50,-51,-54,-55,-58,-77,]),'INT':([3,5,7,14,24,30,35,36,38,43,44,46,47,48,49,50,51,52,62,83,90,114,133,134,135,136,137,139,140,],[8,-67,-69,21,8,-68,8,8,8,-11,-33,8,-20,-15,-16,-17,-18,-19,-34,8,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'FLOAT':([3,5,7,14,24,30,35,36,38,43,44,46,47,48,49,50,51,52,62,83,90,114,133,134,135,136,137,139,140,],[9,-67,-69,22,9,-68,9,9,9,-11,-33,9,-20,-15,-16,-17,-18,-19,-34,9,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'CHAR':([3,5,7,24,30,35,36,38,43,44,46,47,48,49,50,51,52,62,83,90,114,133,134,135,136,137,139,140,],[10,-67,-69,10,-68,10,10,10,-11,-33,10,-20,-15,-16,-17,-18,-19,-34,10,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'FUNCTION':([3,4,5,7,12,13,24,30,43,81,],[-79,14,-67,-69,14,-6,-79,-68,-11,-5,]),'MAIN':([3,4,5,7,11,12,13,19,24,30,43,81,],[-79,-79,-67,-69,18,-79,-4,-3,-79,-68,-11,-5,]),'IF':([5,7,24,30,35,38,43,44,46,47,48,49,50,51,52,62,90,114,133,134,135,136,137,139,140,],[-67,-69,-79,-68,-79,54,-11,-33,54,-20,-15,-16,-17,-18,-19,-34,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'WRITE':([5,7,24,30,35,38,43,44,46,47,48,49,50,51,52,62,90,114,133,134,135,136,137,139,140,],[-67,-69,-79,-68,-79,55,-11,-33,55,-20,-15,-16,-17,-18,-19,-34,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'WHILE':([5,7,24,30,35,38,43,44,46,47,48,49,50,51,52,62,90,114,133,134,135,136,137,139,140,],[-67,-69,-79,-68,-79,56,-11,-33,56,-20,-15,-16,-17,-18,-19,-34,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'RETURN':([5,7,24,30,35,38,43,44,46,47,48,49,50,51,52,62,90,114,133,134,135,136,137,139,140,],[-67,-69,-79,-68,-79,57,-11,-33,57,-20,-15,-16,-17,-18,-19,-34,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'}':([5,7,24,30,35,37,38,43,44,45,46,47,48,49,50,51,52,61,62,90,114,133,134,135,136,137,139,140,],[-67,-69,-79,-68,-79,43,-79,-11,-33,-12,-79,-14,-15,-16,-17,-18,-19,-13,-34,-21,-35,-36,-79,-25,-32,-22,-24,-23,]),'VOID':([14,],[23,]),',':([16,60,],[26,83,]),'(':([18,29,33,54,55,56,57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[28,-7,36,65,66,67,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),')':([28,36,39,40,41,58,60,69,70,71,72,73,75,76,77,78,80,82,84,87,88,89,91,94,95,102,103,106,107,110,111,113,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[32,-79,59,-62,-63,-79,-79,-79,-79,-79,-79,-57,-59,-60,-61,-76,-78,-64,-66,116,117,118,-37,-40,-41,-48,-49,-52,-53,-56,131,-65,-38,-39,-42,-43,-44,-45,-46,-47,-50,-51,-54,-55,-58,-77,]),'{':([32,59,116,118,138,],[35,35,35,35,35,]),'ELSE':([43,134,],[-11,138,]),'=':([53,58,78,80,132,],[63,-79,-76,-78,-77,]),'[':([53,58,78,80,132,],[64,79,-76,-78,-77,]),'CTEF':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'CTEI':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'*':([58,72,73,75,76,77,78,80,131,132,],[-79,108,-57,-59,-60,-61,-76,-78,-58,-77,]),'/':([58,72,73,75,76,77,78,80,131,132,],[-79,109,-57,-59,-60,-61,-76,-78,-58,-77,]),'+':([58,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,104,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'-':([58,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,105,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'<':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,96,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'>':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,97,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'EQUALS':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,98,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'DIFF':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,99,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'LTHANEQ':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,100,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'GTHANEQ':([58,70,71,72,73,75,76,77,78,80,103,106,107,110,127,128,129,130,131,132,],[-79,101,-79,-79,-57,-59,-60,-61,-76,-78,-49,-52,-53,-56,-50,-51,-54,-55,-58,-77,]),'AND':([58,69,70,71,72,73,75,76,77,78,80,95,102,103,106,107,110,121,122,123,124,125,126,127,128,129,130,131,132,],[-79,92,-79,-79,-79,-57,-59,-60,-61,-76,-78,-41,-48,-49,-52,-53,-56,-42,-43,-44,-45,-46,-47,-50,-51,-54,-55,-58,-77,]),'OR':([58,69,70,71,72,73,75,76,77,78,80,95,102,103,106,107,110,121,122,123,124,125,126,127,128,129,130,131,132,],[-79,93,-79,-79,-79,-57,-59,-60,-61,-76,-78,-41,-48,-49,-52,-53,-56,-42,-43,-44,-45,-46,-47,-50,-51,-54,-55,-58,-77,]),']':([58,69,70,71,72,73,75,76,77,78,80,86,91,94,95,102,103,106,107,110,112,119,120,121,122,123,124,125,126,127,128,129,130,131,132,],[-79,-79,-79,-79,-79,-57,-59,-60,-61,-76,-78,115,-37,-40,-41,-48,-49,-52,-53,-56,132,-38,-39,-42,-43,-44,-45,-46,-47,-50,-51,-54,-55,-58,-77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([3,35,38,46,],[4,38,44,44,]),'varsp':([3,24,35,38,46,],[5,30,5,5,5,]),'tipo':([3,24,35,36,38,46,83,],[6,6,6,42,6,6,42,]),'empty':([3,4,12,16,24,35,36,38,46,58,60,69,70,71,72,134,],[7,13,13,27,7,7,41,47,47,80,84,94,102,106,110,139,]),'programaF':([4,12,],[11,19,]),'function':([4,12,],[12,12,]),'varspp':([6,26,],[15,31,]),'main':([11,],[17,]),'tipoRetorno':([14,],[20,]),'varsppp':([16,],[25,]),'functionAux':([29,],[33,]),'bloque':([32,59,116,118,138,],[34,81,134,136,140,]),'cuerpo':([35,],[37,]),'functionParam':([36,],[39,]),'parametro':([36,83,],[40,113,]),'estatutop':([38,46,],[45,61,]),'estatuto':([38,46,],[46,46,]),'asignacion':([38,46,],[48,48,]),'condicion':([38,46,],[49,49,]),'write':([38,46,],[50,50,]),'while':([38,46,],[51,51,]),'return':([38,46,],[52,52,]),'id':([38,46,57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[53,53,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'asignacionp':([53,],[62,]),'superexpresion':([57,63,64,65,66,67,74,79,92,93,],[68,85,86,87,88,89,111,112,119,120,]),'megaexpresion':([57,63,64,65,66,67,74,79,92,93,],[69,69,69,69,69,69,69,69,69,69,]),'exp':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[70,70,70,70,70,70,70,70,70,70,121,122,123,124,125,126,127,128,129,130,]),'termino':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'factor':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'constante':([57,63,64,65,66,67,74,79,92,93,96,97,98,99,100,101,104,105,108,109,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'idp':([58,],[78,]),'parametrop':([60,],[82,]),'superexpresionp':([69,],[91,]),'megaexpresionp':([70,],[95,]),'expp':([71,],[103,]),'terminop':([72,],[107,]),'condicionelse':([134,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ID ; vars programaF main','programa',5,'p_programa','parser.py',15),
  ('main -> MAIN ( ) bloque','main',4,'p_main','parser.py',18),
  ('programaF -> function programaF','programaF',2,'p_programaF','parser.py',21),
  ('programaF -> empty','programaF',1,'p_programaF','parser.py',22),
  ('function -> FUNCTION tipoRetorno ID functionAux ( functionParam ) bloque','function',8,'p_function','parser.py',25),
  ('function -> empty','function',1,'p_function','parser.py',26),
  ('functionAux -> <empty>','functionAux',0,'p_functionAux','parser.py',29),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',45),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',46),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',47),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',52),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',55),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',58),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',59),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',62),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',63),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',64),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',65),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',66),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',67),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',71),
  ('condicion -> IF ( superexpresion ) bloque condicionelse','condicion',6,'p_condicion','parser.py',74),
  ('condicionelse -> ELSE bloque','condicionelse',2,'p_condicionelse','parser.py',77),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',78),
  ('write -> WRITE ( superexpresion ) ;','write',5,'p_write','parser.py',81),
  ('oper -> <','oper',1,'p_oper','parser.py',87),
  ('oper -> >','oper',1,'p_oper','parser.py',88),
  ('oper -> EQUALS','oper',1,'p_oper','parser.py',89),
  ('oper -> DIFF','oper',1,'p_oper','parser.py',90),
  ('oper -> LTHANEQ','oper',1,'p_oper','parser.py',91),
  ('oper -> GTHANEQ','oper',1,'p_oper','parser.py',92),
  ('while -> WHILE ( superexpresion ) bloque','while',5,'p_while','parser.py',95),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',98),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',99),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',102),
  ('asignacionp -> [ superexpresion ] ;','asignacionp',4,'p_asignacionp','parser.py',103),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',106),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',109),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',110),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',111),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',114),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',117),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',118),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',119),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',120),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',121),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',122),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',123),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',126),
  ('expp -> + exp','expp',2,'p_expp','parser.py',129),
  ('expp -> - exp','expp',2,'p_expp','parser.py',130),
  ('expp -> empty','expp',1,'p_expp','parser.py',131),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',134),
  ('terminop -> * exp','terminop',2,'p_terminop','parser.py',137),
  ('terminop -> / exp','terminop',2,'p_terminop','parser.py',138),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',139),
  ('factor -> constante','factor',1,'p_factor','parser.py',142),
  ('factor -> ( superexpresion )','factor',3,'p_factor','parser.py',143),
  ('constante -> id','constante',1,'p_constante','parser.py',146),
  ('constante -> CTEF','constante',1,'p_constante','parser.py',147),
  ('constante -> CTEI','constante',1,'p_constante','parser.py',148),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',151),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',152),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',155),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',162),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',163),
  ('vars -> varsp','vars',1,'p_vars','parser.py',166),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',171),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',172),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',175),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',193),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',194),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',197),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',198),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',199),
  ('id -> ID idp','id',2,'p_id','parser.py',204),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',207),
  ('idp -> empty','idp',1,'p_idp','parser.py',208),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',211),
]
