
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'D7D1BCF469A7160DABB9E0C3456A50E8'
    
_lr_action_items = {'OP_ADD':([15,],[21,]),'STRING':([10,12,13,14,16,17,19,21,22,25,27,28,29,30,31,34,38,39,40,41,42,43,44,45,46,47,51,52,54,55,57,],[13,13,-28,-9,-26,-27,-8,13,13,13,13,13,-30,13,13,-13,-11,13,13,-21,13,13,-29,-22,-24,-12,-10,-23,-20,-25,-19,]),'OP_MUL':([15,],[22,]),'OP_SUB':([15,],[25,]),'OUTPUT':([15,],[23,]),'RPAREN':([11,13,16,17,23,24,27,29,30,31,32,34,35,36,37,38,39,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,],[18,-28,-26,-27,34,38,41,-30,45,46,47,-13,-17,-15,51,-11,52,-21,54,55,-29,-22,-24,-12,-14,-10,-23,57,-20,-25,58,-19,-16,]),'INPUT':([15,],[24,]),'RBRACE':([12,13,14,16,17,19,34,38,41,45,46,47,51,52,54,55,57,],[20,-28,-9,-26,-27,-8,-13,-11,-21,-22,-24,-12,-10,-23,-20,-25,-19,]),'LBRACE':([0,1,2,6,7,8,18,20,],[5,5,-5,-4,-2,-3,-6,-7,]),'$end':([1,2,3,6,7,8,18,20,],[-1,-5,0,-4,-2,-3,-6,-7,]),'IMPORT':([4,],[9,]),'ASSIGN':([15,],[26,]),'LPAREN':([0,1,2,6,7,8,10,12,13,14,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,54,55,57,58,],[4,4,-5,-4,-2,-3,15,15,-28,-9,-26,-27,-6,-8,-7,15,15,33,33,15,15,15,-30,15,15,33,-13,-17,-15,33,-11,15,15,-21,15,15,-29,-22,-24,-12,-14,-10,-23,-20,-25,-19,-16,]),'ID':([5,9,10,12,13,14,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,57,58,],[10,11,16,16,-28,-9,27,-26,-27,-8,16,16,35,35,16,40,16,16,-30,16,16,35,49,-13,-17,-15,35,-11,16,16,-21,16,16,-29,-22,-24,-12,-14,-18,56,-10,-23,-20,-25,-19,-16,]),'NUMBER':([10,12,13,14,16,17,19,21,22,25,27,28,29,30,31,34,38,39,40,41,42,43,44,45,46,47,51,52,54,55,57,],[17,17,-28,-9,-26,-27,-8,17,17,17,17,17,-30,17,17,-13,-11,17,17,-21,17,17,-29,-22,-24,-12,-10,-23,-20,-25,-19,]),'OP_DIV':([15,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([10,12,21,22,25,27,28,30,31,39,40,42,43,],[14,19,29,29,29,29,29,44,44,44,53,44,44,]),'declaration_list':([23,24,],[32,37,]),'parameter_list':([21,22,25,27,28,],[30,31,39,42,43,]),'statement_list':([0,],[1,]),'component':([0,1,],[2,7,]),'program':([0,],[3,]),'declaration':([23,24,32,37,],[36,36,48,48,]),'type':([33,],[50,]),'expression_list':([10,],[12,]),'import_statement':([0,1,],[6,8,]),}

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
