
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BRACKETDER BRACKETIZQ COLON COMMA CTEF CTEI CTESTRING CTESTRING ELSE FLOAT ID IF IGUAL INT INT MASQUE MENOSQUE NOIGUAL PARENDER PARENIZQ PRINT PROGRAM SEMICOLON SIMDIV SIMMAS SIMMENOS SIMMULT VARPROGRAMA : PROGRAM ID SEMICOLON PROGRAMA2 BLOQUEPROGRAMA2 : VARS\n                   | VACIOVARS : VAR VARS2VARS2 : VARS3 COLON TIPO SEMICOLONVARS3 : ID \n            | ID COMMA VARS2TIPO : INT\n            | FLOATBLOQUE : BRACKETIZQ ESTATUTO BRACKETDERESTATUTO : ESTATUTO2 ESTATUTO\n                | VACIOESTATUTO2 : ASIGNACION\n                | CONDICION\n                | ESCRITURAASIGNACION : ID IGUAL EXPRESION SEMICOLONESCRITURA : PRINT PARENIZQ ESCRITURA2 ESCRITURA3 PARENDER SEMICOLONESCRITURA2 : EXPRESION \n                | CTESTRINGESCRITURA3 : COMMA ESCRITURA2 ESCRITURA3\n                | VACIOEXPRESION : EXP EXPRESION2EXPRESION2 : MASQUE EXP\n                | MENOSQUE EXP\n                | NOIGUAL EXP\n                | VACIOCONDICION : IF PARENIZQ EXPRESION PARENDER BLOQUE CONDICION2 SEMICOLONCONDICION2 : ELSE BLOQUE\n                    | VACIOEXP : TERMINO EXP2EXP2 : SIMMAS TERMINO EXP2\n            | SIMMENOS TERMINO EXP2\n            | VACIOTERMINO : FACTOR TERMINO2TERMINO2 : SIMMULT FACTOR TERMINO2\n                | SIMDIV FACTOR TERMINO2\n                | VACIOFACTOR : PARENIZQ EXPRESION PARENDER\n                | FACTOR2 VARCTEFACTOR2 : SIMMAS\n                | SIMMENOS\n                | VACIOVARCTE : ID\n                | CTEI\n                | CTEFVACIO : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,25,],[0,-1,-10,]),'ID':([2,8,10,15,17,18,19,24,27,28,29,38,39,40,41,42,48,50,51,52,55,56,59,60,69,89,91,],[3,13,20,20,-13,-14,-15,13,-46,-46,-46,-46,64,-40,-41,-42,-16,-46,-46,-46,-46,-46,-46,-46,-46,-17,-27,]),'SEMICOLON':([3,25,30,31,32,34,35,36,37,49,53,54,57,58,61,63,64,65,66,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,88,92,],[4,-10,47,-8,-9,48,-46,-46,-46,-22,-26,-30,-33,-34,-37,-39,-43,-44,-45,-23,-24,-25,-46,-46,-46,-46,-38,-46,89,-31,-32,-35,-36,91,-29,-28,]),'VAR':([4,],[8,]),'BRACKETIZQ':([4,5,6,7,11,47,67,87,],[-46,10,-2,-3,-4,-5,10,10,]),'BRACKETDER':([10,14,15,16,17,18,19,26,48,89,91,],[-46,25,-46,-12,-13,-14,-15,-11,-16,-17,-27,]),'IF':([10,15,17,18,19,48,89,91,],[21,21,-13,-14,-15,-16,-17,-27,]),'PRINT':([10,15,17,18,19,48,89,91,],[22,22,-13,-14,-15,-16,-17,-27,]),'COLON':([12,13,33,47,],[23,-6,-7,-5,]),'COMMA':([13,35,36,37,44,45,46,49,53,54,57,58,61,63,64,65,66,71,72,73,74,75,76,77,78,81,82,83,84,85,],[24,-46,-46,-46,69,-18,-19,-22,-26,-30,-33,-34,-37,-39,-43,-44,-45,-23,-24,-25,-46,-46,-46,-46,-38,69,-31,-32,-35,-36,]),'IGUAL':([20,],[27,]),'PARENIZQ':([21,22,27,28,29,38,50,51,52,55,56,59,60,69,],[28,29,38,38,38,38,38,38,38,38,38,38,38,38,]),'INT':([23,],[31,]),'FLOAT':([23,],[32,]),'ELSE':([25,79,],[-10,87,]),'SIMMAS':([27,28,29,36,37,38,50,51,52,55,56,58,59,60,61,63,64,65,66,69,74,75,76,77,78,84,85,],[40,40,40,55,-46,40,40,40,40,40,40,-34,40,40,-37,-39,-43,-44,-45,40,55,55,-46,-46,-38,-35,-36,]),'SIMMENOS':([27,28,29,36,37,38,50,51,52,55,56,58,59,60,61,63,64,65,66,69,74,75,76,77,78,84,85,],[41,41,41,56,-46,41,41,41,41,41,41,-34,41,41,-37,-39,-43,-44,-45,41,56,56,-46,-46,-38,-35,-36,]),'CTEI':([27,28,29,38,39,40,41,42,50,51,52,55,56,59,60,69,],[-46,-46,-46,-46,65,-40,-41,-42,-46,-46,-46,-46,-46,-46,-46,-46,]),'CTEF':([27,28,29,38,39,40,41,42,50,51,52,55,56,59,60,69,],[-46,-46,-46,-46,66,-40,-41,-42,-46,-46,-46,-46,-46,-46,-46,-46,]),'CTESTRING':([29,69,],[46,46,]),'MASQUE':([35,36,37,54,57,58,61,63,64,65,66,74,75,76,77,78,82,83,84,85,],[50,-46,-46,-30,-33,-34,-37,-39,-43,-44,-45,-46,-46,-46,-46,-38,-31,-32,-35,-36,]),'MENOSQUE':([35,36,37,54,57,58,61,63,64,65,66,74,75,76,77,78,82,83,84,85,],[51,-46,-46,-30,-33,-34,-37,-39,-43,-44,-45,-46,-46,-46,-46,-38,-31,-32,-35,-36,]),'NOIGUAL':([35,36,37,54,57,58,61,63,64,65,66,74,75,76,77,78,82,83,84,85,],[52,-46,-46,-30,-33,-34,-37,-39,-43,-44,-45,-46,-46,-46,-46,-38,-31,-32,-35,-36,]),'PARENDER':([35,36,37,43,44,45,46,49,53,54,57,58,61,62,63,64,65,66,68,70,71,72,73,74,75,76,77,78,81,82,83,84,85,90,],[-46,-46,-46,67,-46,-18,-19,-22,-26,-30,-33,-34,-37,78,-39,-43,-44,-45,80,-21,-23,-24,-25,-46,-46,-46,-46,-38,-46,-31,-32,-35,-36,-20,]),'SIMMULT':([37,63,64,65,66,76,77,78,],[59,-39,-43,-44,-45,59,59,-38,]),'SIMDIV':([37,63,64,65,66,76,77,78,],[60,-39,-43,-44,-45,60,60,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'PROGRAMA2':([4,],[5,]),'VARS':([4,],[6,]),'VACIO':([4,10,15,27,28,29,35,36,37,38,44,50,51,52,55,56,59,60,69,74,75,76,77,79,81,],[7,16,16,42,42,42,53,57,61,42,70,42,42,42,42,42,42,42,42,57,57,61,61,88,70,]),'BLOQUE':([5,67,87,],[9,79,92,]),'VARS2':([8,24,],[11,33,]),'VARS3':([8,24,],[12,12,]),'ESTATUTO':([10,15,],[14,26,]),'ESTATUTO2':([10,15,],[15,15,]),'ASIGNACION':([10,15,],[17,17,]),'CONDICION':([10,15,],[18,18,]),'ESCRITURA':([10,15,],[19,19,]),'TIPO':([23,],[30,]),'EXPRESION':([27,28,29,38,69,],[34,43,45,62,45,]),'EXP':([27,28,29,38,50,51,52,69,],[35,35,35,35,71,72,73,35,]),'TERMINO':([27,28,29,38,50,51,52,55,56,69,],[36,36,36,36,36,36,36,74,75,36,]),'FACTOR':([27,28,29,38,50,51,52,55,56,59,60,69,],[37,37,37,37,37,37,37,37,37,76,77,37,]),'FACTOR2':([27,28,29,38,50,51,52,55,56,59,60,69,],[39,39,39,39,39,39,39,39,39,39,39,39,]),'ESCRITURA2':([29,69,],[44,81,]),'EXPRESION2':([35,],[49,]),'EXP2':([36,74,75,],[54,82,83,]),'TERMINO2':([37,76,77,],[58,84,85,]),'VARCTE':([39,],[63,]),'ESCRITURA3':([44,81,],[68,90,]),'CONDICION2':([79,],[86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> PROGRAM ID SEMICOLON PROGRAMA2 BLOQUE','PROGRAMA',5,'p_PROGRAMA','Parser.py',9),
  ('PROGRAMA2 -> VARS','PROGRAMA2',1,'p_PORGRAMA2','Parser.py',13),
  ('PROGRAMA2 -> VACIO','PROGRAMA2',1,'p_PORGRAMA2','Parser.py',14),
  ('VARS -> VAR VARS2','VARS',2,'p_VARS','Parser.py',17),
  ('VARS2 -> VARS3 COLON TIPO SEMICOLON','VARS2',4,'p_VARS2','Parser.py',20),
  ('VARS3 -> ID','VARS3',1,'p_VARS3','Parser.py',23),
  ('VARS3 -> ID COMMA VARS2','VARS3',3,'p_VARS3','Parser.py',24),
  ('TIPO -> INT','TIPO',1,'p_TIPO','Parser.py',27),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','Parser.py',28),
  ('BLOQUE -> BRACKETIZQ ESTATUTO BRACKETDER','BLOQUE',3,'p_BLOQUE','Parser.py',31),
  ('ESTATUTO -> ESTATUTO2 ESTATUTO','ESTATUTO',2,'p_ESTATUTO','Parser.py',34),
  ('ESTATUTO -> VACIO','ESTATUTO',1,'p_ESTATUTO','Parser.py',35),
  ('ESTATUTO2 -> ASIGNACION','ESTATUTO2',1,'p_ESTATUTO2','Parser.py',38),
  ('ESTATUTO2 -> CONDICION','ESTATUTO2',1,'p_ESTATUTO2','Parser.py',39),
  ('ESTATUTO2 -> ESCRITURA','ESTATUTO2',1,'p_ESTATUTO2','Parser.py',40),
  ('ASIGNACION -> ID IGUAL EXPRESION SEMICOLON','ASIGNACION',4,'p_ASIGNACION','Parser.py',43),
  ('ESCRITURA -> PRINT PARENIZQ ESCRITURA2 ESCRITURA3 PARENDER SEMICOLON','ESCRITURA',6,'p_ESCRITURA','Parser.py',46),
  ('ESCRITURA2 -> EXPRESION','ESCRITURA2',1,'p_ESCRITURA2','Parser.py',49),
  ('ESCRITURA2 -> CTESTRING','ESCRITURA2',1,'p_ESCRITURA2','Parser.py',50),
  ('ESCRITURA3 -> COMMA ESCRITURA2 ESCRITURA3','ESCRITURA3',3,'p_ESCRITURA3','Parser.py',53),
  ('ESCRITURA3 -> VACIO','ESCRITURA3',1,'p_ESCRITURA3','Parser.py',54),
  ('EXPRESION -> EXP EXPRESION2','EXPRESION',2,'p_EXPRESION','Parser.py',57),
  ('EXPRESION2 -> MASQUE EXP','EXPRESION2',2,'p_EXPRESION2','Parser.py',60),
  ('EXPRESION2 -> MENOSQUE EXP','EXPRESION2',2,'p_EXPRESION2','Parser.py',61),
  ('EXPRESION2 -> NOIGUAL EXP','EXPRESION2',2,'p_EXPRESION2','Parser.py',62),
  ('EXPRESION2 -> VACIO','EXPRESION2',1,'p_EXPRESION2','Parser.py',63),
  ('CONDICION -> IF PARENIZQ EXPRESION PARENDER BLOQUE CONDICION2 SEMICOLON','CONDICION',7,'p_CONDICION','Parser.py',66),
  ('CONDICION2 -> ELSE BLOQUE','CONDICION2',2,'p_CONDICION2','Parser.py',69),
  ('CONDICION2 -> VACIO','CONDICION2',1,'p_CONDICION2','Parser.py',70),
  ('EXP -> TERMINO EXP2','EXP',2,'p_EXP','Parser.py',73),
  ('EXP2 -> SIMMAS TERMINO EXP2','EXP2',3,'p_EXP2','Parser.py',76),
  ('EXP2 -> SIMMENOS TERMINO EXP2','EXP2',3,'p_EXP2','Parser.py',77),
  ('EXP2 -> VACIO','EXP2',1,'p_EXP2','Parser.py',78),
  ('TERMINO -> FACTOR TERMINO2','TERMINO',2,'p_TERMINO','Parser.py',81),
  ('TERMINO2 -> SIMMULT FACTOR TERMINO2','TERMINO2',3,'p_TERMINO2','Parser.py',84),
  ('TERMINO2 -> SIMDIV FACTOR TERMINO2','TERMINO2',3,'p_TERMINO2','Parser.py',85),
  ('TERMINO2 -> VACIO','TERMINO2',1,'p_TERMINO2','Parser.py',86),
  ('FACTOR -> PARENIZQ EXPRESION PARENDER','FACTOR',3,'p_FACTOR','Parser.py',89),
  ('FACTOR -> FACTOR2 VARCTE','FACTOR',2,'p_FACTOR','Parser.py',90),
  ('FACTOR2 -> SIMMAS','FACTOR2',1,'p_FACTOR2','Parser.py',93),
  ('FACTOR2 -> SIMMENOS','FACTOR2',1,'p_FACTOR2','Parser.py',94),
  ('FACTOR2 -> VACIO','FACTOR2',1,'p_FACTOR2','Parser.py',95),
  ('VARCTE -> ID','VARCTE',1,'p_VARCTE','Parser.py',98),
  ('VARCTE -> CTEI','VARCTE',1,'p_VARCTE','Parser.py',99),
  ('VARCTE -> CTEF','VARCTE',1,'p_VARCTE','Parser.py',100),
  ('VACIO -> <empty>','VACIO',0,'p_VACIO','Parser.py',106),
]
