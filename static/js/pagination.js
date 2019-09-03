#Pagination function

function printClothes(startValue, nPerPage) {
  let endValue = null;
  db.clothes.find( { _id: { $lt: startValue } } )
             .sort( { _id: -1 } )
             .limit( nPerPage )
             .forEach( piece => {
               print( piece.title );
               endValue = piece._id;
             } );

  return endValue;
}