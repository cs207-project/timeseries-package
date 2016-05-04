
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '55C53B9434ED5FC68BBE31AE8D09ED67'
    
_lr_action_items = {'$end':([1,2,5,6,7,8,19,28,],[-1,-4,-5,0,-3,-2,-7,-6,]),'OP_ADD':([13,],[27,]),'LPAREN':([0,1,2,5,7,8,9,11,12,14,15,16,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,51,52,53,54,55,56,58,],[4,4,-4,-5,-3,-2,13,13,-9,-28,-26,-27,-8,-7,13,13,13,35,35,13,13,-6,-30,13,-21,13,13,13,-15,35,-17,-11,35,-13,13,13,-29,-20,-25,-24,-14,-10,-12,-23,-22,-19,-16,]),'STRING':([9,11,12,14,15,16,18,20,21,22,26,27,29,30,31,32,33,34,39,41,42,43,44,45,46,47,52,53,54,55,56,],[14,14,-9,-28,-26,-27,-8,14,14,14,14,14,-30,14,-21,14,14,14,-11,-13,14,14,-29,-20,-25,-24,-10,-12,-23,-22,-19,]),'OP_MUL':([13,],[22,]),'ID':([3,9,10,11,12,13,14,15,16,18,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,58,],[9,15,17,15,-9,20,-28,-26,-27,-8,15,15,15,34,38,38,15,15,-30,15,-21,15,15,15,49,-15,38,-17,-11,38,-13,15,15,-29,-20,-25,-24,-18,57,-14,-10,-12,-23,-22,-19,-16,]),'LBRACE':([0,1,2,5,7,8,19,28,],[3,3,-4,-5,-3,-2,-7,-6,]),'OUTPUT':([13,],[25,]),'IMPORT':([4,],[10,]),'INPUT':([13,],[24,]),'OP_DIV':([13,],[21,]),'OP_SUB':([13,],[26,]),'RPAREN':([14,15,16,17,20,24,25,29,30,31,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,],[-28,-26,-27,28,31,39,41,-30,45,-21,46,47,-15,52,-17,-11,53,-13,54,55,-29,-20,-25,-24,56,-14,-10,-12,-23,-22,-19,58,-16,]),'NUMBER':([9,11,12,14,15,16,18,20,21,22,26,27,29,30,31,32,33,34,39,41,42,43,44,45,46,47,52,53,54,55,56,],[16,16,-9,-28,-26,-27,-8,16,16,16,16,16,-30,16,-21,16,16,16,-11,-13,16,16,-29,-20,-25,-24,-10,-12,-23,-22,-19,]),'RBRACE':([11,12,14,15,16,18,31,39,41,45,46,47,52,53,54,55,56,],[19,-9,-28,-26,-27,-8,-21,-11,-13,-20,-25,-24,-10,-12,-23,-22,-19,]),'ASSIGN':([13,],[23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression_list':([9,],[11,]),'statement_list':([0,],[1,]),'expression':([9,11,20,21,22,26,27,30,32,33,34,42,43,],[12,18,29,29,29,29,29,44,44,44,48,44,44,]),'type':([35,],[50,]),'import_statement':([0,1,],[2,7,]),'component':([0,1,],[5,8,]),'parameter_list':([20,21,22,26,27,],[30,32,33,42,43,]),'program':([0,],[6,]),'declaration':([24,25,37,40,],[36,36,51,51,]),'declaration_list':([24,25,],[37,40,]),}

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
