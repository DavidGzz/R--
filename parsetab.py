
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LETRERO LTHANEQ MAIN OR PROGRAMA RETURN VOID WHILE WRITEprograma : ID primerCuad ';' vars programaF mainprimerCuad : main : MAIN llenarCuad '(' ')' bloquellenarCuad : programaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque functionAux2\n                | emptyfunctionAux : functionAux2 : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | for\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' condicionAux bloque condicionelsecondicionAux : condicionelse : ELSE condicionelseAux bloque\n                        | emptycondicionelseAux : write : WRITE '(' writep ')' ';' writep : superexpresion writepAux writepp\n              | LETRERO writepAux2 writeppwritepAux : writepAux2 : writepp : ',' writeppAux writep\n                | empty writeppAuxwriteppAux : for : FOR '(' id '=' superexpresion ';' superexpresion ')' bloquewhile : WHILE whileAux '(' superexpresion ')' whileAux2 bloquewhileAux : whileAux2 : asignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' '=' superexpresion ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' exp\n            | '-' exp\n            | emptytermino : factor terminopterminop : '*' termino\n                | '/' termino\n                | emptyfactor : constante\n                | lParen superexpresion rParen lParen : '(' rParen : ')' constante : id\n                | CTEF ctef\n                | CTEI cteictef : ctei : functionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '(' idpp ')'\n            | '[' superexpresion ']'\n            | emptyidpp : superexpresion idppp\n            | emptyidppp : ',' idpp\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,6,7,8,9,10,11,21,22,23,24,25,27,31,39,41,45,50,51,53,54,55,56,57,58,59,60,65,71,72,73,74,75,83,87,88,90,91,100,101,103,104,107,108,109,110,111,112,115,116,119,120,130,151,154,157,159,161,168,169,172,173,174,176,178,182,183,],[2,-81,17,-83,-87,-88,-89,30,-11,-12,-13,-98,17,-82,43,-98,67,-14,-43,67,-24,-18,-19,-20,-21,-22,-23,67,-44,67,67,67,67,67,-69,67,67,67,67,-25,67,67,67,67,67,67,67,67,67,67,67,67,-45,67,67,67,-31,-38,-98,67,67,-46,-26,-29,-40,-28,-39,]),'$end':([1,18,40,50,],[0,-1,-3,-14,]),';':([2,3,16,17,26,28,32,67,77,78,79,80,81,82,84,85,86,89,92,94,102,105,106,113,114,117,118,121,123,124,133,137,138,139,140,141,142,143,144,145,146,147,148,149,150,152,156,165,167,],[-2,4,25,-98,-84,-86,-85,-98,101,-98,-98,-98,-98,-67,-71,-74,-75,-90,-93,130,-47,-50,-51,-58,-59,-62,-63,-66,-72,-73,159,-48,-49,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-92,172,173,]),'INT':([4,6,8,15,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[9,-81,-83,22,9,-82,9,9,9,9,-14,-43,9,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'FLOAT':([4,6,8,15,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[10,-81,-83,23,10,-82,10,10,10,10,-14,-43,10,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'CHAR':([4,6,8,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[11,-81,-83,11,-82,11,11,11,11,-14,-43,11,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'FUNCTION':([4,5,6,8,13,14,25,31,50,68,93,],[-98,15,-81,-83,15,-8,-98,-82,-14,-10,-7,]),'MAIN':([4,5,6,8,12,13,14,20,25,31,50,68,93,],[-98,-98,-81,-83,19,-98,-6,-5,-98,-82,-14,-10,-7,]),'IF':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,62,-14,-43,62,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'WRITE':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,63,-14,-43,63,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'WHILE':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,64,-14,-43,64,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'RETURN':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,65,-14,-43,65,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'FOR':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,66,-14,-43,66,-24,-18,-19,-20,-21,-22,-23,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'}':([6,8,25,31,41,44,45,50,51,52,53,54,55,56,57,58,59,60,70,71,101,130,159,168,173,174,176,178,182,183,],[-81,-83,-98,-82,-98,50,-98,-14,-43,-15,-98,-17,-18,-19,-20,-21,-22,-23,-16,-44,-25,-45,-31,-98,-46,-26,-29,-40,-28,-39,]),'VOID':([15,],[24,]),',':([17,43,67,78,79,80,81,82,84,85,86,89,92,98,99,102,105,106,113,114,117,118,121,123,124,127,134,135,137,138,139,140,141,142,143,144,145,146,147,148,149,150,152,156,],[27,48,-98,-98,-98,-98,-98,-67,-71,-74,-75,-90,-93,-34,-35,-47,-50,-51,-58,-59,-62,-63,-66,-72,-73,154,161,161,-48,-49,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-92,]),'(':([19,29,30,62,63,64,65,66,67,72,73,74,75,76,83,87,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,161,169,172,],[-4,33,34,74,75,-41,87,88,90,87,87,87,87,100,87,-69,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,-38,87,87,]),')':([33,34,36,37,38,43,47,49,67,69,78,79,80,81,82,84,85,86,89,90,92,96,97,98,99,102,105,106,113,114,117,118,121,122,123,124,126,127,128,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,152,153,154,155,156,160,162,163,166,170,177,179,],[35,-98,42,-76,-77,-98,-78,-80,-98,-79,-98,-98,-98,-98,-67,-71,-74,-75,-90,-98,-93,132,133,-34,-35,-47,-50,-51,-58,-59,-62,-63,-66,150,-72,-73,152,-98,-95,-98,-98,164,-48,-49,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-94,-98,-97,-92,-32,-38,-33,-96,-37,-36,181,]),'{':([35,42,46,132,158,164,171,175,180,181,],[41,-9,41,-27,41,-42,41,-30,41,41,]),'ELSE':([50,168,],[-14,175,]),'=':([61,67,89,92,125,131,152,156,],[72,-98,-90,-93,151,157,-91,-92,]),'[':([61,67,89,92,152,156,],[73,91,-90,-93,-91,-92,]),'CTEF':([65,72,73,74,75,83,87,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,161,169,172,],[85,85,85,85,85,85,-69,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,-38,85,85,]),'CTEI':([65,72,73,74,75,83,87,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,161,169,172,],[86,86,86,86,86,86,-69,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,-38,86,86,]),'*':([67,81,82,84,85,86,89,92,123,124,149,150,152,156,],[-98,119,-67,-71,-74,-75,-90,-93,-72,-73,-68,-70,-91,-92,]),'/':([67,81,82,84,85,86,89,92,123,124,149,150,152,156,],[-98,120,-67,-71,-74,-75,-90,-93,-72,-73,-68,-70,-91,-92,]),'+':([67,80,81,82,84,85,86,89,92,118,121,123,124,147,148,149,150,152,156,],[-98,115,-98,-67,-71,-74,-75,-90,-93,-63,-66,-72,-73,-64,-65,-68,-70,-91,-92,]),'-':([67,80,81,82,84,85,86,89,92,118,121,123,124,147,148,149,150,152,156,],[-98,116,-98,-67,-71,-74,-75,-90,-93,-63,-66,-72,-73,-64,-65,-68,-70,-91,-92,]),'<':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,107,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'>':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,108,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'EQUALS':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,109,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'DIFF':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,110,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'LTHANEQ':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,111,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'GTHANEQ':([67,79,80,81,82,84,85,86,89,92,114,117,118,121,123,124,145,146,147,148,149,150,152,156,],[-98,112,-98,-98,-67,-71,-74,-75,-90,-93,-59,-62,-63,-66,-72,-73,-60,-61,-64,-65,-68,-70,-91,-92,]),'AND':([67,78,79,80,81,82,84,85,86,89,92,106,113,114,117,118,121,123,124,139,140,141,142,143,144,145,146,147,148,149,150,152,156,],[-98,103,-98,-98,-98,-67,-71,-74,-75,-90,-93,-51,-58,-59,-62,-63,-66,-72,-73,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-92,]),'OR':([67,78,79,80,81,82,84,85,86,89,92,106,113,114,117,118,121,123,124,139,140,141,142,143,144,145,146,147,148,149,150,152,156,],[-98,104,-98,-98,-98,-67,-71,-74,-75,-90,-93,-51,-58,-59,-62,-63,-66,-72,-73,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-92,]),']':([67,78,79,80,81,82,84,85,86,89,92,95,102,105,106,113,114,117,118,121,123,124,129,137,138,139,140,141,142,143,144,145,146,147,148,149,150,152,156,],[-98,-98,-98,-98,-98,-67,-71,-74,-75,-90,-93,131,-47,-50,-51,-58,-59,-62,-63,-66,-72,-73,156,-48,-49,-52,-53,-54,-55,-56,-57,-60,-61,-64,-65,-68,-70,-91,-92,]),'LETRERO':([75,161,169,],[99,-38,99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'primerCuad':([2,],[3,]),'vars':([4,41,45,53,],[5,45,51,51,]),'varsp':([4,25,41,45,53,],[6,31,6,6,6,]),'tipo':([4,25,34,41,45,48,53,],[7,7,39,7,7,39,7,]),'empty':([4,5,13,17,25,34,41,43,45,53,67,78,79,80,81,90,127,134,135,154,168,],[8,14,14,28,8,38,8,49,54,54,92,105,113,117,121,128,155,162,162,128,176,]),'programaF':([5,13,],[12,20,]),'function':([5,13,],[13,13,]),'varspp':([7,27,],[16,32,]),'main':([12,],[18,]),'tipoRetorno':([15,],[21,]),'varsppp':([17,],[26,]),'llenarCuad':([19,],[29,]),'functionParam':([34,],[36,]),'parametro':([34,48,],[37,69,]),'bloque':([35,46,158,171,180,181,],[40,68,168,178,182,183,]),'cuerpo':([41,],[44,]),'functionAux':([42,],[46,]),'parametrop':([43,],[47,]),'estatutop':([45,53,],[52,70,]),'estatuto':([45,53,],[53,53,]),'asignacion':([45,53,],[55,55,]),'condicion':([45,53,],[56,56,]),'write':([45,53,],[57,57,]),'while':([45,53,],[58,58,]),'return':([45,53,],[59,59,]),'for':([45,53,],[60,60,]),'id':([45,53,65,72,73,74,75,83,88,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,169,172,],[61,61,84,84,84,84,84,84,125,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'asignacionp':([61,],[71,]),'whileAux':([64,],[76,]),'superexpresion':([65,72,73,74,75,83,90,91,100,103,104,151,154,157,169,172,],[77,94,95,96,98,122,127,129,136,137,138,165,127,167,98,179,]),'megaexpresion':([65,72,73,74,75,83,90,91,100,103,104,151,154,157,169,172,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'exp':([65,72,73,74,75,83,90,91,100,103,104,107,108,109,110,111,112,115,116,151,154,157,169,172,],[79,79,79,79,79,79,79,79,79,79,79,139,140,141,142,143,144,145,146,79,79,79,79,79,]),'termino':([65,72,73,74,75,83,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,169,172,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,147,148,80,80,80,80,80,]),'factor':([65,72,73,74,75,83,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,169,172,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'constante':([65,72,73,74,75,83,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,169,172,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'lParen':([65,72,73,74,75,83,90,91,100,103,104,107,108,109,110,111,112,115,116,119,120,151,154,157,169,172,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'idp':([67,],[89,]),'functionAux2':([68,],[93,]),'writep':([75,169,],[97,177,]),'superexpresionp':([78,],[102,]),'megaexpresionp':([79,],[106,]),'expp':([80,],[114,]),'terminop':([81,],[118,]),'ctef':([85,],[123,]),'ctei':([86,],[124,]),'idpp':([90,154,],[126,166,]),'writepAux':([98,],[134,]),'writepAux2':([99,],[135,]),'rParen':([122,],[149,]),'idppp':([127,],[153,]),'condicionAux':([132,],[158,]),'writepp':([134,135,],[160,163,]),'writeppAux':([161,162,],[169,170,]),'whileAux2':([164,],[171,]),'condicionelse':([168,],[174,]),'condicionelseAux':([175,],[180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ID primerCuad ; vars programaF main','programa',6,'p_programa','parser.py',34),
  ('primerCuad -> <empty>','primerCuad',0,'p_primerCuad','parser.py',37),
  ('main -> MAIN llenarCuad ( ) bloque','main',5,'p_main','parser.py',41),
  ('llenarCuad -> <empty>','llenarCuad',0,'p_llenarCuad','parser.py',44),
  ('programaF -> function programaF','programaF',2,'p_programaF','parser.py',48),
  ('programaF -> empty','programaF',1,'p_programaF','parser.py',49),
  ('function -> FUNCTION tipoRetorno ID ( functionParam ) functionAux bloque functionAux2','function',9,'p_function','parser.py',52),
  ('function -> empty','function',1,'p_function','parser.py',53),
  ('functionAux -> <empty>','functionAux',0,'p_functionAux','parser.py',56),
  ('functionAux2 -> <empty>','functionAux2',0,'p_functionAux2','parser.py',71),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',83),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',84),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',85),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',89),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',92),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',95),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',96),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',99),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',100),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',101),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',102),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',103),
  ('estatuto -> for','estatuto',1,'p_estatuto','parser.py',104),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',105),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',108),
  ('condicion -> IF ( superexpresion ) condicionAux bloque condicionelse','condicion',7,'p_condicion','parser.py',122),
  ('condicionAux -> <empty>','condicionAux',0,'p_condicionAux','parser.py',125),
  ('condicionelse -> ELSE condicionelseAux bloque','condicionelse',3,'p_condicionelse','parser.py',135),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',136),
  ('condicionelseAux -> <empty>','condicionelseAux',0,'p_condicionelseAux','parser.py',141),
  ('write -> WRITE ( writep ) ;','write',5,'p_write','parser.py',148),
  ('writep -> superexpresion writepAux writepp','writep',3,'p_writep','parser.py',151),
  ('writep -> LETRERO writepAux2 writepp','writep',3,'p_writep','parser.py',152),
  ('writepAux -> <empty>','writepAux',0,'p_writepAux','parser.py',155),
  ('writepAux2 -> <empty>','writepAux2',0,'p_writepAux2','parser.py',160),
  ('writepp -> , writeppAux writep','writepp',3,'p_writepp','parser.py',167),
  ('writepp -> empty writeppAux','writepp',2,'p_writepp','parser.py',168),
  ('writeppAux -> <empty>','writeppAux',0,'p_writeppAux','parser.py',171),
  ('for -> FOR ( id = superexpresion ; superexpresion ) bloque','for',9,'p_for','parser.py',179),
  ('while -> WHILE whileAux ( superexpresion ) whileAux2 bloque','while',7,'p_while','parser.py',182),
  ('whileAux -> <empty>','whileAux',0,'p_whileAux','parser.py',189),
  ('whileAux2 -> <empty>','whileAux2',0,'p_whileAux2','parser.py',193),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',202),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',203),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',206),
  ('asignacionp -> [ superexpresion ] = superexpresion ;','asignacionp',6,'p_asignacionp','parser.py',207),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',213),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',230),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',231),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',232),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',237),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',253),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',254),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',255),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',256),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',257),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',258),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',259),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',264),
  ('expp -> + exp','expp',2,'p_expp','parser.py',282),
  ('expp -> - exp','expp',2,'p_expp','parser.py',283),
  ('expp -> empty','expp',1,'p_expp','parser.py',284),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',293),
  ('terminop -> * termino','terminop',2,'p_terminop','parser.py',311),
  ('terminop -> / termino','terminop',2,'p_terminop','parser.py',312),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',313),
  ('factor -> constante','factor',1,'p_factor','parser.py',318),
  ('factor -> lParen superexpresion rParen','factor',3,'p_factor','parser.py',319),
  ('lParen -> (','lParen',1,'p_lParen','parser.py',322),
  ('rParen -> )','rParen',1,'p_rParen','parser.py',326),
  ('constante -> id','constante',1,'p_constante','parser.py',330),
  ('constante -> CTEF ctef','constante',2,'p_constante','parser.py',331),
  ('constante -> CTEI ctei','constante',2,'p_constante','parser.py',332),
  ('ctef -> <empty>','ctef',0,'p_ctef','parser.py',335),
  ('ctei -> <empty>','ctei',0,'p_ctei','parser.py',341),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',347),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',348),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',351),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',357),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',358),
  ('vars -> varsp','vars',1,'p_vars','parser.py',361),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',366),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',367),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',370),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',390),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',391),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',394),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',395),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',396),
  ('id -> ID idp','id',2,'p_id','parser.py',400),
  ('idp -> ( idpp )','idp',3,'p_idp','parser.py',403),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',404),
  ('idp -> empty','idp',1,'p_idp','parser.py',405),
  ('idpp -> superexpresion idppp','idpp',2,'p_idpp','parser.py',433),
  ('idpp -> empty','idpp',1,'p_idpp','parser.py',434),
  ('idppp -> , idpp','idppp',2,'p_idppp','parser.py',437),
  ('idppp -> empty','idppp',1,'p_idppp','parser.py',438),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',443),
]
