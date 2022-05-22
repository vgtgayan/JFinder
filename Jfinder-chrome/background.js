//when update tab call fillForm function

chrome.runtime.onInstalled.addListener(function () {

    pdata = []
    chrome.storage.sync.set({"autoFill":"true"}, function () {
        //close();        
    });

});



chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    chrome.storage.sync.get("autoFill", function (data) {
        if (data.autoFill) {
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                chrome.tabs.sendMessage(tabs[0].id, {
                    action: "fillForm"
                });
            });
        }
    });
});

chrome.storage.onChanged.addListener(function (tabId, changeInfo, tab) {
    chrome.storage.sync.get("autoFill", function (data) {
        if (data.autoFill) {
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                chrome.tabs.sendMessage(tabs[0].id, {
                    action: "fillForm"
                });
            });
        }
    });
});