#!/usr/bin/node

/* lets code*/
exports.esrever = function (list) {
  const backList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    backList.push(list[i]);
  }
  return backList;
};
