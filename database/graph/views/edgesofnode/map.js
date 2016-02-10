function(doc) {
  if (doc.entrytype && doc.entrytype == 'link'){
    emit(doc.source,  [doc.target, doc.length]);
}
}
