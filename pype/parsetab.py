
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'E1FCB2EDDF1216D4CA039394CC93A7CE'
    
_lr_action_items = {'LBRACE':([0,2,3,6,8,9,27,28,],[1,-5,1,-4,-2,-3,-7,-6,]),'ASSIGN':([12,],[18,]),'RPAREN':([13,14,16,17,23,24,25,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,],[-27,-26,-28,28,35,38,43,-30,45,47,48,49,-21,50,51,-13,-17,-15,55,-11,56,-25,-29,-22,-23,-24,-20,-12,-14,-10,-19,58,-16,]),'OP_DIV':([12,],[19,]),'OP_ADD':([12,],[20,]),'OP_SUB':([12,],[21,]),'OP_MUL':([12,],[22,]),'ID':([1,7,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,58,],[7,14,17,-9,23,-27,-26,14,-28,29,14,14,14,14,14,39,39,-8,14,-30,14,14,14,14,-21,14,39,-13,-17,-15,53,39,-11,-25,-29,-22,-23,-24,-20,-12,-14,-18,57,-10,-19,-16,]),'NUMBER':([7,11,13,14,15,16,19,20,21,22,23,26,29,30,31,32,33,34,35,36,38,43,45,46,47,48,49,50,51,55,56,],[13,-9,-27,-26,13,-28,13,13,13,13,13,-8,13,-30,13,13,13,13,-21,13,-13,-11,-25,-29,-22,-23,-24,-20,-12,-10,-19,]),'RBRACE':([11,13,14,15,16,26,35,38,43,45,47,48,49,50,51,55,56,],[-9,-27,-26,27,-28,-8,-21,-13,-11,-25,-22,-23,-24,-20,-12,-10,-19,]),'LPAREN':([0,2,3,6,7,8,9,11,13,14,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,45,46,47,48,49,50,51,52,55,56,58,],[5,-5,5,-4,12,-2,-3,-9,-27,-26,12,-28,12,12,12,12,12,41,41,-8,-7,-6,12,-30,12,12,12,12,-21,12,41,-13,-17,-15,41,-11,-25,-29,-22,-23,-24,-20,-12,-14,-10,-19,-16,]),'OUTPUT':([12,],[24,]),'IMPORT':([5,],[10,]),'STRING':([7,11,13,14,15,16,19,20,21,22,23,26,29,30,31,32,33,34,35,36,38,43,45,46,47,48,49,50,51,55,56,],[16,-9,-27,-26,16,-28,16,16,16,16,16,-8,16,-30,16,16,16,16,-21,16,-13,-11,-25,-29,-22,-23,-24,-20,-12,-10,-19,]),'INPUT':([12,],[25,]),'$end':([2,3,4,6,8,9,27,28,],[-5,-1,0,-4,-2,-3,-7,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'component':([0,3,],[2,8,]),'declaration_list':([24,25,],[37,42,]),'expression_list':([7,],[15,]),'statement_list':([0,],[3,]),'program':([0,],[4,]),'parameter_list':([19,20,21,22,23,],[31,32,33,34,36,]),'expression':([7,15,19,20,21,22,23,29,31,32,33,34,36,],[11,26,30,30,30,30,30,44,46,46,46,46,46,]),'type':([41,],[54,]),'declaration':([24,25,37,42,],[40,40,52,52,]),'import_statement':([0,3,],[6,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',7),
  ('statement_list -> statement_list component','statement_list',2,'p_statement_list','parser.py',12),
  ('statement_list -> statement_list import_statement','statement_list',2,'p_statement_list','parser.py',13),
  ('statement_list -> import_statement','statement_list',1,'p_statement_list','parser.py',14),
  ('statement_list -> component','statement_list',1,'p_statement_list','parser.py',15),
  ('import_statement -> LPAREN IMPORT ID RPAREN','import_statement',4,'p_import_statement','parser.py',26),
  ('component -> LBRACE ID expression_list RBRACE','component',4,'p_component','parser.py',30),
  ('expression_list -> expression_list expression','expression_list',2,'p_expression_list','parser.py',34),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',35),
  ('expression -> LPAREN INPUT declaration_list RPAREN','expression',4,'p_expression_input','parser.py',44),
  ('expression -> LPAREN INPUT RPAREN','expression',3,'p_expression_input','parser.py',45),
  ('expression -> LPAREN OUTPUT declaration_list RPAREN','expression',4,'p_expression_output','parser.py',52),
  ('expression -> LPAREN OUTPUT RPAREN','expression',3,'p_expression_output','parser.py',53),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',60),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parser.py',61),
  ('declaration -> LPAREN type ID RPAREN','declaration',4,'p_declaration','parser.py',70),
  ('declaration -> ID','declaration',1,'p_declaration','parser.py',71),
  ('type -> ID','type',1,'p_type','parser.py',79),
  ('expression -> LPAREN ASSIGN ID expression RPAREN','expression',5,'p_expression_assign','parser.py',83),
  ('expression -> LPAREN ID parameter_list RPAREN','expression',4,'p_expression_parameter_list','parser.py',87),
  ('expression -> LPAREN ID RPAREN','expression',3,'p_expression_parameter_list','parser.py',88),
  ('expression -> LPAREN OP_ADD parameter_list RPAREN','expression',4,'p_op_add_expression','parser.py',96),
  ('expression -> LPAREN OP_SUB parameter_list RPAREN','expression',4,'p_op_sub_expression','parser.py',100),
  ('expression -> LPAREN OP_MUL parameter_list RPAREN','expression',4,'p_op_mul_expression','parser.py',104),
  ('expression -> LPAREN OP_DIV parameter_list RPAREN','expression',4,'p_op_div_expression','parser.py',108),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',112),
  ('expression -> NUMBER','expression',1,'p_expression_num','parser.py',116),
  ('expression -> STRING','expression',1,'p_expression_str','parser.py',120),
  ('parameter_list -> parameter_list expression','parameter_list',2,'p_parameter_list','parser.py',124),
  ('parameter_list -> expression','parameter_list',1,'p_parameter_list','parser.py',125),
]
