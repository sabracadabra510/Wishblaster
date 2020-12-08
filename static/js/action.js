// alert("Javascript connected!")
$('#view-list').on('submit', (evt) =>{
    evt.preventDefault();
    const formInputs = {
       'family_members_wishlist_id':$('#person-name').val()
    }
    $.post('/view_wishlist.json', formInputs, (res) => {
        console.log(res);
        for (const item of res) {
            $('#magic').append(`<p>Item: ${item.item_name}</p>`);
            $('#magic').append(`      Website Link: ${item.item_link}`);
        }
      });
})