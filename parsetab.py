
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR CTEF CTEI CUADRATICA DIFF ELSE EQUALS FACT FIBONACCI FLOAT FOR FUNCTION GTHANEQ ID IF INT LETRERO LTHANEQ MAIN OR RAIZ RETURN VOID WHILE WRITEprograma : ID primerCuad ';' vars programaF mainprimerCuad : main : MAIN llenarCuad '(' ')' bloquellenarCuad : programaF : function programaF\n                    | emptyfunction : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque functionAux2\n                | emptyfunctionAux : functionAux2 : tipoRetorno : INT\n                    | FLOAT\n                    | VOIDbloque : '{' cuerpo '}' cuerpo : vars estatutopestatutop : estatuto estatutop\n                    | emptyestatuto : asignacion\n                    | condicion\n                    | write\n                    | while\n                    | return\n                    | for\n                    | fact\n                    | fibonacci\n                    | cuadratica\n                    | raiz\n                    | id ';'\n                    | emptyreturn : RETURN '(' superexpresion ')' ';' condicion : IF '(' superexpresion ')' condicionAux bloque condicionelsecondicionAux : condicionelse : ELSE condicionelseAux bloque\n                        | emptycondicionelseAux : write : WRITE '(' writep ')' ';' writep : superexpresion writepAux writepp\n              | LETRERO writepAux2 writeppwritepAux : writepAux2 : writepp : ',' writeppAux writep\n                | empty writeppAuxwriteppAux : for : FOR '(' id '=' superexpresion forAux ';' superexpresion forAux2 ';' asignacion ')' bloque forAux3forAux : forAux2 : forAux3 : while : WHILE whileAux '(' superexpresion ')' whileAux2 bloquewhileAux : whileAux2 : asignacion : vars\n                    | id asignacionpasignacionp : '=' superexpresion ';' superexpresion : megaexpresion superexpresionpsuperexpresionp : AND superexpresion\n                        | OR superexpresion\n                        | emptymegaexpresion : exp megaexpresionpmegaexpresionp : '<' exp\n                        | '>' exp\n                        | EQUALS exp\n                        | DIFF exp\n                        | LTHANEQ exp\n                        | GTHANEQ exp\n                        | emptyexp : termino exppexpp : '+' pAppT exp\n            | '-' pAppT exp\n            | emptypAppT : termino : factor terminopterminop : '*' pAppF termino\n                | '/' pAppF termino\n                | emptypAppF : factor : constante\n                | lParen superexpresion rParen lParen : '(' rParen : ')' constante : id\n                | CTEF ctef\n                | CTEI cteictef : ctei : functionParam : parametro\n                    | emptyparametro : tipo ID parametropparametrop : ',' parametro\n                | emptyvars : varspvarsp : tipo varspp ';' varsp\n                | emptyvarspp : ID varspppvarsppp : ',' varspp\n                | '[' CTEI ']' arreglo\n                | emptyarreglo : ',' varspp\n                | emptytipo : INT\n            | FLOAT\n            | CHARid : ID idpidp : '(' idpp ')'\n            | '[' superexpresion ']'\n            | emptyidpp : superexpresion idppp\n            | emptyidppp : ',' idpp\n            | emptyfact : FACT '(' CTEI ')' ';' cuadratica : CUADRATICA '(' CTEI ',' CTEI ',' CTEI ')' ';' fibonacci : FIBONACCI '(' CTEI ')' ';' raiz : RAIZ '(' CTEI ')' ';' empty :"
    
_lr_action_items = {'ID':([0,6,7,8,9,10,11,21,22,23,24,25,27,32,42,44,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,88,89,90,92,93,99,100,109,113,118,129,131,132,135,136,137,138,139,140,143,144,147,148,159,166,177,178,179,180,184,186,190,192,193,195,201,202,207,209,211,212,217,219,220,224,225,],[2,-90,17,-92,-99,-100,-101,31,-11,-12,-13,-114,17,-91,49,17,-114,82,-14,-51,82,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,82,82,82,82,82,82,82,82,-78,82,-53,82,82,82,82,82,82,82,82,-70,-70,-75,-75,82,82,82,82,82,82,-36,-43,-30,-110,-112,-113,-114,82,-31,-34,-48,82,-33,-111,82,-47,-44,]),'$end':([1,18,46,57,],[0,-1,-3,-14,]),';':([2,3,16,17,26,29,33,37,43,45,50,72,82,98,101,103,104,105,106,107,108,110,111,112,130,133,134,141,142,145,146,149,151,152,154,158,160,161,163,164,168,169,170,171,172,173,174,175,176,181,182,191,197,198,199,200,205,215,216,218,],[-2,4,25,-114,-93,-96,-94,-114,-95,-98,-97,86,-114,-102,-105,129,-114,-114,-114,-114,-76,-80,-83,-84,-54,-57,-58,-65,-66,-69,-71,-74,-81,-82,184,190,192,193,195,-103,-104,-55,-56,-59,-60,-61,-62,-63,-64,-77,-79,-45,-67,-68,-72,-73,212,-46,219,220,]),'INT':([4,6,8,15,25,32,36,47,52,55,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,220,224,225,],[9,-90,-92,22,9,-91,9,9,9,9,-14,-51,9,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,9,-47,-44,]),'FLOAT':([4,6,8,15,25,32,36,47,52,55,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,220,224,225,],[10,-90,-92,23,10,-91,10,10,10,10,-14,-51,10,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,10,-47,-44,]),'CHAR':([4,6,8,25,32,36,47,52,55,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,220,224,225,],[11,-90,-92,11,-91,11,11,11,11,-14,-51,11,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,11,-47,-44,]),'FUNCTION':([4,5,6,8,13,14,25,32,57,83,102,],[-114,15,-90,-92,15,-8,-114,-91,-14,-10,-7,]),'MAIN':([4,5,6,8,12,13,14,20,25,32,57,83,102,],[-114,-114,-90,-92,19,-114,-6,-5,-114,-91,-14,-10,-7,]),'IF':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,73,-14,-51,73,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'WRITE':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,74,-14,-51,74,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'WHILE':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,75,-14,-51,75,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'RETURN':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,76,-14,-51,76,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'FOR':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,77,-14,-51,77,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'FACT':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,78,-14,-51,78,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'FIBONACCI':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,79,-14,-51,79,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'CUADRATICA':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,80,-14,-51,80,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'RAIZ':([6,8,25,32,47,52,57,58,60,61,62,63,64,65,66,67,68,69,70,71,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,81,-14,-51,81,-29,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),'}':([6,8,25,32,47,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,85,86,87,129,184,190,192,193,195,201,207,209,211,217,219,224,225,],[-90,-92,-114,-91,-114,57,-114,-14,-51,-15,-114,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-16,-28,-52,-53,-36,-30,-110,-112,-113,-114,-31,-34,-48,-33,-111,-47,-44,]),')':([6,8,25,32,35,36,39,40,41,49,54,56,58,82,84,87,98,99,101,104,105,106,107,108,110,111,112,114,115,116,117,119,121,122,124,125,126,127,129,130,133,134,141,142,145,146,149,150,151,152,155,156,157,164,165,166,167,168,169,170,171,172,173,174,175,176,181,182,185,187,188,196,197,198,199,200,203,210,213,220,222,],[-90,-92,-114,-91,38,-114,48,-85,-86,-114,-87,-89,-51,-114,-88,-52,-102,-114,-105,-114,-114,-114,-114,-76,-80,-83,-84,153,154,-39,-40,158,160,161,163,164,-114,-107,-53,-54,-57,-58,-65,-66,-69,-71,-74,182,-81,-82,-114,-114,189,-103,-106,-114,-109,-104,-55,-56,-59,-60,-61,-62,-63,-64,-77,-79,-37,-43,-38,-108,-67,-68,-72,-73,-42,-41,216,-114,223,]),'VOID':([15,],[24,]),',':([17,37,49,82,98,101,104,105,106,107,108,110,111,112,116,117,123,126,130,133,134,141,142,145,146,149,151,152,155,156,164,168,169,170,171,172,173,174,175,176,181,182,194,197,198,199,200,],[27,44,55,-114,-102,-105,-114,-114,-114,-114,-76,-80,-83,-84,-39,-40,162,166,-54,-57,-58,-65,-66,-69,-71,-74,-81,-82,186,186,-103,-104,-55,-56,-59,-60,-61,-62,-63,-64,-77,-79,206,-67,-68,-72,-73,]),'[':([17,82,],[28,100,]),'(':([19,30,31,73,74,75,76,77,78,79,80,81,82,88,89,90,91,92,99,100,109,113,118,131,132,135,136,137,138,139,140,143,144,147,148,159,166,177,178,179,180,186,202,212,],[-4,35,36,89,90,-49,92,93,94,95,96,97,99,113,113,113,118,113,113,113,113,-78,113,113,113,113,113,113,113,113,113,-70,-70,-75,-75,113,113,113,113,113,113,-43,113,113,]),'CTEI':([28,88,89,90,92,94,95,96,97,99,100,109,113,118,131,132,135,136,137,138,139,140,143,144,147,148,159,162,166,177,178,179,180,186,202,206,212,],[34,112,112,112,112,121,122,123,124,112,112,112,-78,112,112,112,112,112,112,112,112,112,-70,-70,-75,-75,112,194,112,112,112,112,112,-43,112,213,112,]),']':([34,82,98,101,104,105,106,107,108,110,111,112,128,130,133,134,141,142,145,146,149,151,152,164,168,169,170,171,172,173,174,175,176,181,182,197,198,199,200,],[37,-114,-102,-105,-114,-114,-114,-114,-76,-80,-83,-84,168,-54,-57,-58,-65,-66,-69,-71,-74,-81,-82,-103,-104,-55,-56,-59,-60,-61,-62,-63,-64,-77,-79,-67,-68,-72,-73,]),'{':([38,48,53,153,183,189,204,208,214,223,],[47,-9,47,-32,47,-50,47,-35,47,47,]),'ELSE':([57,201,],[-14,208,]),'=':([72,82,98,101,120,164,168,221,],[88,-114,-102,-105,159,-103,-104,88,]),'*':([82,98,101,107,108,110,111,112,151,152,164,168,181,182,],[-114,-102,-105,147,-76,-80,-83,-84,-81,-82,-103,-104,-77,-79,]),'/':([82,98,101,107,108,110,111,112,151,152,164,168,181,182,],[-114,-102,-105,148,-76,-80,-83,-84,-81,-82,-103,-104,-77,-79,]),'+':([82,98,101,106,107,108,110,111,112,146,149,151,152,164,168,181,182,199,200,],[-114,-102,-105,143,-114,-76,-80,-83,-84,-71,-74,-81,-82,-103,-104,-77,-79,-72,-73,]),'-':([82,98,101,106,107,108,110,111,112,146,149,151,152,164,168,181,182,199,200,],[-114,-102,-105,144,-114,-76,-80,-83,-84,-71,-74,-81,-82,-103,-104,-77,-79,-72,-73,]),'<':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,135,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'>':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,136,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'EQUALS':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,137,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'DIFF':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,138,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'LTHANEQ':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,139,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'GTHANEQ':([82,98,101,105,106,107,108,110,111,112,142,145,146,149,151,152,164,168,181,182,197,198,199,200,],[-114,-102,-105,140,-114,-114,-76,-80,-83,-84,-66,-69,-71,-74,-81,-82,-103,-104,-77,-79,-67,-68,-72,-73,]),'AND':([82,98,101,104,105,106,107,108,110,111,112,134,141,142,145,146,149,151,152,164,168,171,172,173,174,175,176,181,182,197,198,199,200,],[-114,-102,-105,131,-114,-114,-114,-76,-80,-83,-84,-58,-65,-66,-69,-71,-74,-81,-82,-103,-104,-59,-60,-61,-62,-63,-64,-77,-79,-67,-68,-72,-73,]),'OR':([82,98,101,104,105,106,107,108,110,111,112,134,141,142,145,146,149,151,152,164,168,171,172,173,174,175,176,181,182,197,198,199,200,],[-114,-102,-105,132,-114,-114,-114,-76,-80,-83,-84,-58,-65,-66,-69,-71,-74,-81,-82,-103,-104,-59,-60,-61,-62,-63,-64,-77,-79,-67,-68,-72,-73,]),'CTEF':([88,89,90,92,99,100,109,113,118,131,132,135,136,137,138,139,140,143,144,147,148,159,166,177,178,179,180,186,202,212,],[111,111,111,111,111,111,111,-78,111,111,111,111,111,111,111,111,111,-70,-70,-75,-75,111,111,111,111,111,111,-43,111,111,]),'LETRERO':([90,186,202,],[117,-43,117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'primerCuad':([2,],[3,]),'vars':([4,47,52,60,220,],[5,52,58,58,58,]),'varsp':([4,25,47,52,60,220,],[6,32,6,6,6,6,]),'tipo':([4,25,36,47,52,55,60,220,],[7,7,42,7,7,42,7,7,]),'empty':([4,5,13,17,25,36,37,47,49,52,60,82,99,104,105,106,107,126,155,156,166,201,220,],[8,14,14,29,8,41,45,8,56,61,61,101,127,133,141,145,149,167,187,187,127,209,8,]),'programaF':([5,13,],[12,20,]),'function':([5,13,],[13,13,]),'varspp':([7,27,44,],[16,33,50,]),'main':([12,],[18,]),'tipoRetorno':([15,],[21,]),'varsppp':([17,],[26,]),'llenarCuad':([19,],[30,]),'functionParam':([36,],[39,]),'parametro':([36,55,],[40,84,]),'arreglo':([37,],[43,]),'bloque':([38,53,183,204,214,223,],[46,83,201,211,217,224,]),'cuerpo':([47,],[51,]),'functionAux':([48,],[53,]),'parametrop':([49,],[54,]),'estatutop':([52,60,],[59,85,]),'estatuto':([52,60,],[60,60,]),'asignacion':([52,60,220,],[62,62,222,]),'condicion':([52,60,],[63,63,]),'write':([52,60,],[64,64,]),'while':([52,60,],[65,65,]),'return':([52,60,],[66,66,]),'for':([52,60,],[67,67,]),'fact':([52,60,],[68,68,]),'fibonacci':([52,60,],[69,69,]),'cuadratica':([52,60,],[70,70,]),'raiz':([52,60,],[71,71,]),'id':([52,60,88,89,90,92,93,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,179,180,202,212,220,],[72,72,110,110,110,110,120,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,221,]),'asignacionp':([72,221,],[87,87,]),'whileAux':([75,],[91,]),'idp':([82,],[98,]),'functionAux2':([83,],[102,]),'superexpresion':([88,89,90,92,99,100,109,118,131,132,159,166,202,212,],[103,114,116,119,126,128,150,157,169,170,191,126,116,215,]),'megaexpresion':([88,89,90,92,99,100,109,118,131,132,159,166,202,212,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'exp':([88,89,90,92,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,202,212,],[105,105,105,105,105,105,105,105,105,105,171,172,173,174,175,176,105,105,197,198,105,105,]),'termino':([88,89,90,92,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,179,180,202,212,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,199,200,106,106,]),'factor':([88,89,90,92,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,179,180,202,212,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'constante':([88,89,90,92,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,179,180,202,212,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'lParen':([88,89,90,92,99,100,109,118,131,132,135,136,137,138,139,140,159,166,177,178,179,180,202,212,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'writep':([90,202,],[115,210,]),'idpp':([99,166,],[125,196,]),'superexpresionp':([104,],[130,]),'megaexpresionp':([105,],[134,]),'expp':([106,],[142,]),'terminop':([107,],[146,]),'ctef':([111,],[151,]),'ctei':([112,],[152,]),'writepAux':([116,],[155,]),'writepAux2':([117,],[156,]),'idppp':([126,],[165,]),'pAppT':([143,144,],[177,178,]),'pAppF':([147,148,],[179,180,]),'rParen':([150,],[181,]),'condicionAux':([153,],[183,]),'writepp':([155,156,],[185,188,]),'writeppAux':([186,187,],[202,203,]),'whileAux2':([189,],[204,]),'forAux':([191,],[205,]),'condicionelse':([201,],[207,]),'condicionelseAux':([208,],[214,]),'forAux2':([215,],[218,]),'forAux3':([224,],[225,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ID primerCuad ; vars programaF main','programa',6,'p_programa','parser.py',34),
  ('primerCuad -> <empty>','primerCuad',0,'p_primerCuad','parser.py',38),
  ('main -> MAIN llenarCuad ( ) bloque','main',5,'p_main','parser.py',42),
  ('llenarCuad -> <empty>','llenarCuad',0,'p_llenarCuad','parser.py',46),
  ('programaF -> function programaF','programaF',2,'p_programaF','parser.py',50),
  ('programaF -> empty','programaF',1,'p_programaF','parser.py',51),
  ('function -> FUNCTION tipoRetorno ID ( functionParam ) functionAux bloque functionAux2','function',9,'p_function','parser.py',54),
  ('function -> empty','function',1,'p_function','parser.py',55),
  ('functionAux -> <empty>','functionAux',0,'p_functionAux','parser.py',58),
  ('functionAux2 -> <empty>','functionAux2',0,'p_functionAux2','parser.py',75),
  ('tipoRetorno -> INT','tipoRetorno',1,'p_tipoRetorno','parser.py',98),
  ('tipoRetorno -> FLOAT','tipoRetorno',1,'p_tipoRetorno','parser.py',99),
  ('tipoRetorno -> VOID','tipoRetorno',1,'p_tipoRetorno','parser.py',100),
  ('bloque -> { cuerpo }','bloque',3,'p_bloque','parser.py',104),
  ('cuerpo -> vars estatutop','cuerpo',2,'p_cuerpo','parser.py',107),
  ('estatutop -> estatuto estatutop','estatutop',2,'p_estatutop','parser.py',110),
  ('estatutop -> empty','estatutop',1,'p_estatutop','parser.py',111),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser.py',114),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','parser.py',115),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser.py',116),
  ('estatuto -> while','estatuto',1,'p_estatuto','parser.py',117),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser.py',118),
  ('estatuto -> for','estatuto',1,'p_estatuto','parser.py',119),
  ('estatuto -> fact','estatuto',1,'p_estatuto','parser.py',120),
  ('estatuto -> fibonacci','estatuto',1,'p_estatuto','parser.py',121),
  ('estatuto -> cuadratica','estatuto',1,'p_estatuto','parser.py',122),
  ('estatuto -> raiz','estatuto',1,'p_estatuto','parser.py',123),
  ('estatuto -> id ;','estatuto',2,'p_estatuto','parser.py',124),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',125),
  ('return -> RETURN ( superexpresion ) ;','return',5,'p_return','parser.py',128),
  ('condicion -> IF ( superexpresion ) condicionAux bloque condicionelse','condicion',7,'p_condicion','parser.py',143),
  ('condicionAux -> <empty>','condicionAux',0,'p_condicionAux','parser.py',146),
  ('condicionelse -> ELSE condicionelseAux bloque','condicionelse',3,'p_condicionelse','parser.py',159),
  ('condicionelse -> empty','condicionelse',1,'p_condicionelse','parser.py',160),
  ('condicionelseAux -> <empty>','condicionelseAux',0,'p_condicionelseAux','parser.py',166),
  ('write -> WRITE ( writep ) ;','write',5,'p_write','parser.py',174),
  ('writep -> superexpresion writepAux writepp','writep',3,'p_writep','parser.py',177),
  ('writep -> LETRERO writepAux2 writepp','writep',3,'p_writep','parser.py',178),
  ('writepAux -> <empty>','writepAux',0,'p_writepAux','parser.py',181),
  ('writepAux2 -> <empty>','writepAux2',0,'p_writepAux2','parser.py',186),
  ('writepp -> , writeppAux writep','writepp',3,'p_writepp','parser.py',193),
  ('writepp -> empty writeppAux','writepp',2,'p_writepp','parser.py',194),
  ('writeppAux -> <empty>','writeppAux',0,'p_writeppAux','parser.py',197),
  ('for -> FOR ( id = superexpresion forAux ; superexpresion forAux2 ; asignacion ) bloque forAux3','for',14,'p_for','parser.py',206),
  ('forAux -> <empty>','forAux',0,'p_forAux','parser.py',209),
  ('forAux2 -> <empty>','forAux2',0,'p_forAux2','parser.py',216),
  ('forAux3 -> <empty>','forAux3',0,'p_forAux3','parser.py',223),
  ('while -> WHILE whileAux ( superexpresion ) whileAux2 bloque','while',7,'p_while','parser.py',230),
  ('whileAux -> <empty>','whileAux',0,'p_whileAux','parser.py',238),
  ('whileAux2 -> <empty>','whileAux2',0,'p_whileAux2','parser.py',243),
  ('asignacion -> vars','asignacion',1,'p_asignacion','parser.py',253),
  ('asignacion -> id asignacionp','asignacion',2,'p_asignacion','parser.py',254),
  ('asignacionp -> = superexpresion ;','asignacionp',3,'p_asignacionp','parser.py',257),
  ('superexpresion -> megaexpresion superexpresionp','superexpresion',2,'p_superexpresion','parser.py',263),
  ('superexpresionp -> AND superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',283),
  ('superexpresionp -> OR superexpresion','superexpresionp',2,'p_superexpresionp','parser.py',284),
  ('superexpresionp -> empty','superexpresionp',1,'p_superexpresionp','parser.py',285),
  ('megaexpresion -> exp megaexpresionp','megaexpresion',2,'p_megaexpresion','parser.py',290),
  ('megaexpresionp -> < exp','megaexpresionp',2,'p_megaexpresionp','parser.py',306),
  ('megaexpresionp -> > exp','megaexpresionp',2,'p_megaexpresionp','parser.py',307),
  ('megaexpresionp -> EQUALS exp','megaexpresionp',2,'p_megaexpresionp','parser.py',308),
  ('megaexpresionp -> DIFF exp','megaexpresionp',2,'p_megaexpresionp','parser.py',309),
  ('megaexpresionp -> LTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',310),
  ('megaexpresionp -> GTHANEQ exp','megaexpresionp',2,'p_megaexpresionp','parser.py',311),
  ('megaexpresionp -> empty','megaexpresionp',1,'p_megaexpresionp','parser.py',312),
  ('exp -> termino expp','exp',2,'p_exp','parser.py',317),
  ('expp -> + pAppT exp','expp',3,'p_expp','parser.py',335),
  ('expp -> - pAppT exp','expp',3,'p_expp','parser.py',336),
  ('expp -> empty','expp',1,'p_expp','parser.py',337),
  ('pAppT -> <empty>','pAppT',0,'p_pAppT','parser.py',342),
  ('termino -> factor terminop','termino',2,'p_termino','parser.py',360),
  ('terminop -> * pAppF termino','terminop',3,'p_terminop','parser.py',378),
  ('terminop -> / pAppF termino','terminop',3,'p_terminop','parser.py',379),
  ('terminop -> empty','terminop',1,'p_terminop','parser.py',380),
  ('pAppF -> <empty>','pAppF',0,'p_pAppF','parser.py',385),
  ('factor -> constante','factor',1,'p_factor','parser.py',408),
  ('factor -> lParen superexpresion rParen','factor',3,'p_factor','parser.py',409),
  ('lParen -> (','lParen',1,'p_lParen','parser.py',412),
  ('rParen -> )','rParen',1,'p_rParen','parser.py',416),
  ('constante -> id','constante',1,'p_constante','parser.py',420),
  ('constante -> CTEF ctef','constante',2,'p_constante','parser.py',421),
  ('constante -> CTEI ctei','constante',2,'p_constante','parser.py',422),
  ('ctef -> <empty>','ctef',0,'p_ctef','parser.py',425),
  ('ctei -> <empty>','ctei',0,'p_ctei','parser.py',433),
  ('functionParam -> parametro','functionParam',1,'p_functionParam','parser.py',439),
  ('functionParam -> empty','functionParam',1,'p_functionParam','parser.py',440),
  ('parametro -> tipo ID parametrop','parametro',3,'p_parametro','parser.py',443),
  ('parametrop -> , parametro','parametrop',2,'p_parametrop','parser.py',450),
  ('parametrop -> empty','parametrop',1,'p_parametrop','parser.py',451),
  ('vars -> varsp','vars',1,'p_vars','parser.py',454),
  ('varsp -> tipo varspp ; varsp','varsp',4,'p_varsp','parser.py',460),
  ('varsp -> empty','varsp',1,'p_varsp','parser.py',461),
  ('varspp -> ID varsppp','varspp',2,'p_varspp','parser.py',464),
  ('varsppp -> , varspp','varsppp',2,'p_varsppp','parser.py',485),
  ('varsppp -> [ CTEI ] arreglo','varsppp',4,'p_varsppp','parser.py',486),
  ('varsppp -> empty','varsppp',1,'p_varsppp','parser.py',487),
  ('arreglo -> , varspp','arreglo',2,'p_arreglo','parser.py',490),
  ('arreglo -> empty','arreglo',1,'p_arreglo','parser.py',491),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',495),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',496),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',497),
  ('id -> ID idp','id',2,'p_id','parser.py',501),
  ('idp -> ( idpp )','idp',3,'p_idp','parser.py',504),
  ('idp -> [ superexpresion ]','idp',3,'p_idp','parser.py',505),
  ('idp -> empty','idp',1,'p_idp','parser.py',506),
  ('idpp -> superexpresion idppp','idpp',2,'p_idpp','parser.py',541),
  ('idpp -> empty','idpp',1,'p_idpp','parser.py',542),
  ('idppp -> , idpp','idppp',2,'p_idppp','parser.py',545),
  ('idppp -> empty','idppp',1,'p_idppp','parser.py',546),
  ('fact -> FACT ( CTEI ) ;','fact',5,'p_fact','parser.py',552),
  ('cuadratica -> CUADRATICA ( CTEI , CTEI , CTEI ) ;','cuadratica',9,'p_cuadratica','parser.py',556),
  ('fibonacci -> FIBONACCI ( CTEI ) ;','fibonacci',5,'p_fibonacci','parser.py',560),
  ('raiz -> RAIZ ( CTEI ) ;','raiz',5,'p_raiz','parser.py',564),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',569),
]
