def get_num_tp(actls,preds):
  return len([i for i,l in enumerate(preds) if l==1 and l==actls[i]])

def get_num_tn(actls,preds):
  return len([i for i,l in enumerate(preds) if l==0 and l==actls[i]])

def get_num_fp(actls,preds):
  return len([i for i,l in enumerate(preds) if l==1 and l!=actls[i]])

def get_num_fn(actls,preds):
  return len([i for i,l in enumerate(preds) if l==0 and l!=actls[i]])

def get_recall_macro(actls,preds):
  tp = get_num_tp(actls,preds)
  tn = get_num_tn(actls,preds)
  num_actual_positives = len([i for i in actls if i == 1])
  num_actual_negatives = len(actls) - num_actual_positives
  positive_class_recall = tp/num_actual_positives
  negative_class_recall = tn/num_actual_negatives
  return (positive_class_recall+negative_class_recall)/2

def get_precision_macro(actls,preds):
  tp = get_num_tp(actls,preds)
  tn = get_num_tn(actls,preds)
  num_pred_positives = len([i for i in preds if i == 1])
  num_pred_negatives = len(preds) - num_pred_positives
  positive_class_precision = tp/num_pred_positives
  negative_class_precision = tn/num_pred_negatives
  return (positive_class_precision + negative_class_precision)/2

def get_f1_macro(actls,preds):
  return (get_precision_macro(actls,preds) + get_recall_macro(actls,preds))/2

def get_mcc_score(actls,preds):
  tp = get_num_tp(actls,preds)
  tn = get_num_tn(actls,preds)
  fp = get_num_fp(actls,preds)
  fn = get_num_fn(actls,preds)
  mcc_bolunen = tp*tn - fp*fn
  mcc_bolen = (tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)
  return mcc_bolunen/mcc_bolen