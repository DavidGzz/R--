
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR CTEF CTEI DIFF ELSE EQUALS FLOAT FOR FUNCTION GTHANEQ ID IF INT LETRERO LTHANEQ MAIN OR RETURN VOID WHILE WRITEprograma : ID primerCuad ';' vars programaF mainprimerCuad : main : MAIN llenarCuad '(' ')' bloquellenarCuad : programaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque functionAux2\n                | emptyfunctionAux : functionAux2 : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | for\n                    | id ';'\n                    | emptyreturn : RETURN superexpresion ';' condicion : IF '(' superexpresion ')' condicionAux bloque condicionelsecondicionAux : condicionelse : ELSE condicionelseAux bloque\n                        | emptycondicionelseAux : write : WRITE '(' writep ')' ';' writep : superexpresion writepAux writepp\n              | LETRERO writepAux2 writeppwritepAux : writepAux2 : writepp : ',' writeppAux writep\n                | empty writeppAuxwriteppAux : for : FOR '(' id '=' superexpresion ';' superexpresion ')' bloquewhile : WHILE whileAux '(' superexpresion ')' whileAux2 bloquewhileAux : whileAux2 : asignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';'\n                    | '[' superexpresion ']' '=' superexpresion ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' pAppT exp\n            | '-' pAppT exp\n            | emptypAppT : termino : factor terminopterminop : '*' pAppF termino\n                | '/' pAppF termino\n                | emptypAppF : factor : constante\n                | lParen superexpresion rParen lParen : '(' rParen : ')' constante : id\n                | CTEF ctef\n                | CTEI cteictef : ctei : functionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '(' idpp ')'\n            | '[' superexpresion ']'\n            | emptyidpp : superexpresion idppp\n            | emptyidppp : ',' idpp\n            | emptyempty :"
    
_lr_action_items = {'ID':([0,6,7,8,9,10,11,21,22,23,24,25,27,31,39,41,45,50,51,53,54,55,56,57,58,59,60,65,71,72,73,74,75,76,84,88,89,91,92,101,102,104,105,108,109,110,111,112,113,116,117,120,121,131,146,147,148,149,152,155,158,160,162,173,174,177,178,179,181,183,187,188,],[2,-84,17,-86,-90,-91,-92,30,-11,-12,-13,-101,17,-85,43,-101,67,-14,-44,67,-25,-18,-19,-20,-21,-22,-23,67,-24,-45,67,67,67,67,67,-72,67,67,67,67,-26,67,67,67,67,67,67,67,67,-64,-64,-69,-69,-46,67,67,67,67,67,67,67,-32,-39,-101,67,67,-47,-27,-30,-41,-29,-40,]),'$end':([1,18,40,50,],[0,-1,-3,-14,]),';':([2,3,16,17,26,28,32,61,67,78,79,80,81,82,83,85,86,87,90,93,95,103,106,107,114,115,118,119,122,124,125,134,138,139,140,141,142,143,144,145,150,151,153,157,166,167,168,169,170,172,],[-2,4,25,-101,-87,-89,-88,71,-101,102,-101,-101,-101,-101,-70,-74,-77,-78,-93,-96,131,-48,-51,-52,-59,-60,-63,-65,-68,-75,-76,160,-49,-50,-53,-54,-55,-56,-57,-58,-71,-73,-94,-95,-61,-62,-66,-67,177,178,]),'INT':([4,6,8,15,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[9,-84,-86,22,9,-85,9,9,9,9,-14,-44,9,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'FLOAT':([4,6,8,15,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[10,-84,-86,23,10,-85,10,10,10,10,-14,-44,10,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'CHAR':([4,6,8,25,31,34,41,45,48,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[11,-84,-86,11,-85,11,11,11,11,-14,-44,11,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'FUNCTION':([4,5,6,8,13,14,25,31,50,68,94,],[-101,15,-84,-86,15,-8,-101,-85,-14,-10,-7,]),'MAIN':([4,5,6,8,12,13,14,20,25,31,50,68,94,],[-101,-101,-84,-86,19,-101,-6,-5,-101,-85,-14,-10,-7,]),'IF':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,62,-14,-44,62,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'WRITE':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,63,-14,-44,63,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'WHILE':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,64,-14,-44,64,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'RETURN':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,65,-14,-44,65,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'FOR':([6,8,25,31,41,45,50,51,53,54,55,56,57,58,59,60,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,66,-14,-44,66,-25,-18,-19,-20,-21,-22,-23,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'}':([6,8,25,31,41,44,45,50,51,52,53,54,55,56,57,58,59,60,70,71,72,102,131,160,173,178,179,181,183,187,188,],[-84,-86,-101,-85,-101,50,-101,-14,-44,-15,-101,-17,-18,-19,-20,-21,-22,-23,-16,-24,-45,-26,-46,-32,-101,-47,-27,-30,-41,-29,-40,]),'VOID':([15,],[24,]),',':([17,43,67,79,80,81,82,83,85,86,87,90,93,99,100,103,106,107,114,115,118,119,122,124,125,128,135,136,138,139,140,141,142,143,144,145,150,151,153,157,166,167,168,169,],[27,48,-101,-101,-101,-101,-101,-70,-74,-77,-78,-93,-96,-35,-36,-48,-51,-52,-59,-60,-63,-65,-68,-75,-76,155,162,162,-49,-50,-53,-54,-55,-56,-57,-58,-71,-73,-94,-95,-61,-62,-66,-67,]),'(':([19,29,30,62,63,64,65,66,67,73,74,75,76,77,84,88,91,92,101,104,105,108,109,110,111,112,113,116,117,120,121,146,147,148,149,152,155,158,162,174,177,],[-4,33,34,75,76,-42,88,89,91,88,88,88,88,101,88,-72,88,88,88,88,88,88,88,88,88,88,88,-64,-64,-69,-69,88,88,88,88,88,88,88,-39,88,88,]),')':([33,34,36,37,38,43,47,49,67,69,79,80,81,82,83,85,86,87,90,91,93,97,98,99,100,103,106,107,114,115,118,119,122,123,124,125,127,128,129,135,136,137,138,139,140,141,142,143,144,145,150,151,153,154,155,156,157,161,163,164,166,167,168,169,171,175,182,184,],[35,-101,42,-79,-80,-101,-81,-83,-101,-82,-101,-101,-101,-101,-70,-74,-77,-78,-93,-101,-96,133,134,-35,-36,-48,-51,-52,-59,-60,-63,-65,-68,151,-75,-76,153,-101,-98,-101,-101,165,-49,-50,-53,-54,-55,-56,-57,-58,-71,-73,-94,-97,-101,-100,-95,-33,-39,-34,-61,-62,-66,-67,-99,-38,-37,186,]),'{':([35,42,46,133,159,165,176,180,185,186,],[41,-9,41,-28,41,-43,41,-31,41,41,]),'ELSE':([50,173,],[-14,180,]),'=':([61,67,90,93,126,132,153,157,],[73,-101,-93,-96,152,158,-94,-95,]),'[':([61,67,90,93,153,157,],[74,92,-93,-96,-94,-95,]),'CTEF':([65,73,74,75,76,84,88,91,92,101,104,105,108,109,110,111,112,113,116,117,120,121,146,147,148,149,152,155,158,162,174,177,],[86,86,86,86,86,86,-72,86,86,86,86,86,86,86,86,86,86,86,-64,-64,-69,-69,86,86,86,86,86,86,86,-39,86,86,]),'CTEI':([65,73,74,75,76,84,88,91,92,101,104,105,108,109,110,111,112,113,116,117,120,121,146,147,148,149,152,155,158,162,174,177,],[87,87,87,87,87,87,-72,87,87,87,87,87,87,87,87,87,87,87,-64,-64,-69,-69,87,87,87,87,87,87,87,-39,87,87,]),'*':([67,82,83,85,86,87,90,93,124,125,150,151,153,157,],[-101,120,-70,-74,-77,-78,-93,-96,-75,-76,-71,-73,-94,-95,]),'/':([67,82,83,85,86,87,90,93,124,125,150,151,153,157,],[-101,121,-70,-74,-77,-78,-93,-96,-75,-76,-71,-73,-94,-95,]),'+':([67,81,82,83,85,86,87,90,93,119,122,124,125,150,151,153,157,168,169,],[-101,116,-101,-70,-74,-77,-78,-93,-96,-65,-68,-75,-76,-71,-73,-94,-95,-66,-67,]),'-':([67,81,82,83,85,86,87,90,93,119,122,124,125,150,151,153,157,168,169,],[-101,117,-101,-70,-74,-77,-78,-93,-96,-65,-68,-75,-76,-71,-73,-94,-95,-66,-67,]),'<':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,108,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'>':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,109,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'EQUALS':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,110,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'DIFF':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,111,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'LTHANEQ':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,112,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'GTHANEQ':([67,80,81,82,83,85,86,87,90,93,115,118,119,122,124,125,150,151,153,157,166,167,168,169,],[-101,113,-101,-101,-70,-74,-77,-78,-93,-96,-60,-63,-65,-68,-75,-76,-71,-73,-94,-95,-61,-62,-66,-67,]),'AND':([67,79,80,81,82,83,85,86,87,90,93,107,114,115,118,119,122,124,125,140,141,142,143,144,145,150,151,153,157,166,167,168,169,],[-101,104,-101,-101,-101,-70,-74,-77,-78,-93,-96,-52,-59,-60,-63,-65,-68,-75,-76,-53,-54,-55,-56,-57,-58,-71,-73,-94,-95,-61,-62,-66,-67,]),'OR':([67,79,80,81,82,83,85,86,87,90,93,107,114,115,118,119,122,124,125,140,141,142,143,144,145,150,151,153,157,166,167,168,169,],[-101,105,-101,-101,-101,-70,-74,-77,-78,-93,-96,-52,-59,-60,-63,-65,-68,-75,-76,-53,-54,-55,-56,-57,-58,-71,-73,-94,-95,-61,-62,-66,-67,]),']':([67,79,80,81,82,83,85,86,87,90,93,96,103,106,107,114,115,118,119,122,124,125,130,138,139,140,141,142,143,144,145,150,151,153,157,166,167,168,169,],[-101,-101,-101,-101,-101,-70,-74,-77,-78,-93,-96,132,-48,-51,-52,-59,-60,-63,-65,-68,-75,-76,157,-49,-50,-53,-54,-55,-56,-57,-58,-71,-73,-94,-95,-61,-62,-66,-67,]),'LETRERO':([76,162,174,],[100,-39,100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'primerCuad':([2,],[3,]),'vars':([4,41,45,53,],[5,45,51,51,]),'varsp':([4,25,41,45,53,],[6,31,6,6,6,]),'tipo':([4,25,34,41,45,48,53,],[7,7,39,7,7,39,7,]),'empty':([4,5,13,17,25,34,41,43,45,53,67,79,80,81,82,91,128,135,136,155,173,],[8,14,14,28,8,38,8,49,54,54,93,106,114,118,122,129,156,163,163,129,181,]),'programaF':([5,13,],[12,20,]),'function':([5,13,],[13,13,]),'varspp':([7,27,],[16,32,]),'main':([12,],[18,]),'tipoRetorno':([15,],[21,]),'varsppp':([17,],[26,]),'llenarCuad':([19,],[29,]),'functionParam':([34,],[36,]),'parametro':([34,48,],[37,69,]),'bloque':([35,46,159,176,185,186,],[40,68,173,183,187,188,]),'cuerpo':([41,],[44,]),'functionAux':([42,],[46,]),'parametrop':([43,],[47,]),'estatutop':([45,53,],[52,70,]),'estatuto':([45,53,],[53,53,]),'asignacion':([45,53,],[55,55,]),'condicion':([45,53,],[56,56,]),'write':([45,53,],[57,57,]),'while':([45,53,],[58,58,]),'return':([45,53,],[59,59,]),'for':([45,53,],[60,60,]),'id':([45,53,65,73,74,75,76,84,89,91,92,101,104,105,108,109,110,111,112,113,146,147,148,149,152,155,158,174,177,],[61,61,85,85,85,85,85,85,126,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'asignacionp':([61,],[72,]),'whileAux':([64,],[77,]),'superexpresion':([65,73,74,75,76,84,91,92,101,104,105,152,155,158,174,177,],[78,95,96,97,99,123,128,130,137,138,139,170,128,172,99,184,]),'megaexpresion':([65,73,74,75,76,84,91,92,101,104,105,152,155,158,174,177,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'exp':([65,73,74,75,76,84,91,92,101,104,105,108,109,110,111,112,113,146,147,152,155,158,174,177,],[80,80,80,80,80,80,80,80,80,80,80,140,141,142,143,144,145,166,167,80,80,80,80,80,]),'termino':([65,73,74,75,76,84,91,92,101,104,105,108,109,110,111,112,113,146,147,148,149,152,155,158,174,177,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,168,169,81,81,81,81,81,]),'factor':([65,73,74,75,76,84,91,92,101,104,105,108,109,110,111,112,113,146,147,148,149,152,155,158,174,177,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'constante':([65,73,74,75,76,84,91,92,101,104,105,108,109,110,111,112,113,146,147,148,149,152,155,158,174,177,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'lParen':([65,73,74,75,76,84,91,92,101,104,105,108,109,110,111,112,113,146,147,148,149,152,155,158,174,177,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'idp':([67,],[90,]),'functionAux2':([68,],[94,]),'writep':([76,174,],[98,182,]),'superexpresionp':([79,],[103,]),'megaexpresionp':([80,],[107,]),'expp':([81,],[115,]),'terminop':([82,],[119,]),'ctef':([86,],[124,]),'ctei':([87,],[125,]),'idpp':([91,155,],[127,171,]),'writepAux':([99,],[135,]),'writepAux2':([100,],[136,]),'pAppT':([116,117,],[146,147,]),'pAppF':([120,121,],[148,149,]),'rParen':([123,],[150,]),'idppp':([128,],[154,]),'condicionAux':([133,],[159,]),'writepp':([135,136,],[161,164,]),'writeppAux':([162,163,],[174,175,]),'whileAux2':([165,],[176,]),'condicionelse':([173,],[179,]),'condicionelseAux':([180,],[185,]),}

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
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',91),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',92),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',93),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',97),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',100),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',103),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',104),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',107),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',108),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',109),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',110),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',111),
  ('estatuto -> for','estatuto',1,'p_estatuto','parser.py',112),
  ('estatuto -> id ;','estatuto',2,'p_estatuto','parser.py',113),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',114),
  ('return -> RETURN superexpresion ;','return',3,'p_return','parser.py',117),
  ('condicion -> IF ( superexpresion ) condicionAux bloque condicionelse','condicion',7,'p_condicion','parser.py',132),
  ('condicionAux -> <empty>','condicionAux',0,'p_condicionAux','parser.py',135),
  ('condicionelse -> ELSE condicionelseAux bloque','condicionelse',3,'p_condicionelse','parser.py',145),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',146),
  ('condicionelseAux -> <empty>','condicionelseAux',0,'p_condicionelseAux','parser.py',151),
  ('write -> WRITE ( writep ) ;','write',5,'p_write','parser.py',158),
  ('writep -> superexpresion writepAux writepp','writep',3,'p_writep','parser.py',161),
  ('writep -> LETRERO writepAux2 writepp','writep',3,'p_writep','parser.py',162),
  ('writepAux -> <empty>','writepAux',0,'p_writepAux','parser.py',165),
  ('writepAux2 -> <empty>','writepAux2',0,'p_writepAux2','parser.py',170),
  ('writepp -> , writeppAux writep','writepp',3,'p_writepp','parser.py',177),
  ('writepp -> empty writeppAux','writepp',2,'p_writepp','parser.py',178),
  ('writeppAux -> <empty>','writeppAux',0,'p_writeppAux','parser.py',181),
  ('for -> FOR ( id = superexpresion ; superexpresion ) bloque','for',9,'p_for','parser.py',189),
  ('while -> WHILE whileAux ( superexpresion ) whileAux2 bloque','while',7,'p_while','parser.py',192),
  ('whileAux -> <empty>','whileAux',0,'p_whileAux','parser.py',199),
  ('whileAux2 -> <empty>','whileAux2',0,'p_whileAux2','parser.py',203),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',212),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',213),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',216),
  ('asignacionp -> [ superexpresion ] = superexpresion ;','asignacionp',6,'p_asignacionp','parser.py',217),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',223),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',240),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',241),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',242),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',247),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',263),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',264),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',265),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',266),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',267),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',268),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',269),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',274),
  ('expp -> + pAppT exp','expp',3,'p_expp','parser.py',292),
  ('expp -> - pAppT exp','expp',3,'p_expp','parser.py',293),
  ('expp -> empty','expp',1,'p_expp','parser.py',294),
  ('pAppT -> <empty>','pAppT',0,'p_pAppT','parser.py',299),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',317),
  ('terminop -> * pAppF termino','terminop',3,'p_terminop','parser.py',335),
  ('terminop -> / pAppF termino','terminop',3,'p_terminop','parser.py',336),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',337),
  ('pAppF -> <empty>','pAppF',0,'p_pAppF','parser.py',342),
  ('factor -> constante','factor',1,'p_factor','parser.py',365),
  ('factor -> lParen superexpresion rParen','factor',3,'p_factor','parser.py',366),
  ('lParen -> (','lParen',1,'p_lParen','parser.py',369),
  ('rParen -> )','rParen',1,'p_rParen','parser.py',373),
  ('constante -> id','constante',1,'p_constante','parser.py',377),
  ('constante -> CTEF ctef','constante',2,'p_constante','parser.py',378),
  ('constante -> CTEI ctei','constante',2,'p_constante','parser.py',379),
  ('ctef -> <empty>','ctef',0,'p_ctef','parser.py',382),
  ('ctei -> <empty>','ctei',0,'p_ctei','parser.py',388),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',394),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',395),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',398),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',404),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',405),
  ('vars -> varsp','vars',1,'p_vars','parser.py',408),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',413),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',414),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',417),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',437),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',438),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',441),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',442),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',443),
  ('id -> ID idp','id',2,'p_id','parser.py',447),
  ('idp -> ( idpp )','idp',3,'p_idp','parser.py',450),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',451),
  ('idp -> empty','idp',1,'p_idp','parser.py',452),
  ('idpp -> superexpresion idppp','idpp',2,'p_idpp','parser.py',481),
  ('idpp -> empty','idpp',1,'p_idpp','parser.py',482),
  ('idppp -> , idpp','idppp',2,'p_idppp','parser.py',485),
  ('idppp -> empty','idppp',1,'p_idppp','parser.py',486),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',491),
]
