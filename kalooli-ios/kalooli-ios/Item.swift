//
//  Item.swift
//  kalooli-ios
//
//  Created by Noel Brathen on 7/28/25.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
