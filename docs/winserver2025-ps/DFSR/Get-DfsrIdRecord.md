---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsridrecord?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrIdRecord
---

# 获取 DFSR ID 记录

## 摘要
从DFS复制数据库中获取已复制文件或文件夹的ID记录。

## 语法

### PathParameterSet（默认值）
```
Get-DfsrIdRecord [-Path] <String[]> [[-ComputerName] <String>] [<CommonParameters>]
```

### UidParameterSet
```
Get-DfsrIdRecord [-Uid] <String[]> [[-ComputerName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrIdRecord` cmdlet 用于从分布式文件系统（DFS）复制数据库中获取已复制文件或文件夹的 ID 记录。可以指定唯一的标识符（UID）或文件路径。一个 UID 由一个 GUID 和一个版本值组成。

## 示例

### 示例 1：获取指定路径的 ID 记录
```
PS C:\> Get-DfsrIdRecord -Path "C:\RF01\Accounting 2013.xlsx"
Identifier                  : {031C15B7-397D-4F99-A340-B1C7931EEE01}-v12
Flags                       : 5
Attributes                  : 32
GlobalVersionSequenceNumber : {9F159608-2199-4D8B-B9F5-51D83A778089}-v11
UpdateSequenceNumber        : 77158344
ParentId                    : {1D69BB80-C1DC-4D87-8259-BBD9639C2A7F}-v1
FileId                      : 562949953494937
Volume                      : \\.\C:
Fence                       : 3
Clock                       : 130096051943887948
CreateTime                  : 4/4/2013 6:26:59 PM
UpdateTime                  : 4/4/2013 8:13:14 PM
FileHash                    : 89de8fbaba0b700b 9b2a6b771ee17921
FileName                    : accounting 2013.xlsx
FullPathName                : C:\RF01\Accounting 2013.xlsx
Index                       : 4
ReplicatedFolderId          : 1d69bb80-c1dc-4d87-8259-bbd9639c2a7f
```

该命令用于获取由文件路径 C:\RF01\Accounting 2013.xlsx 指定的文件的ID记录。

## 参数

### -ComputerName
指定复制成员计算机的名称。如果未指定此参数，cmdlet 将使用当前计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定一组文件或文件夹的路径。如果指定了此参数，请不要指定 *Uid* 参数。

```yaml
Type: String[]
Parameter Sets: PathParameterSet
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -Uid
指定一组文件或文件夹的 UID（唯一标识符）。如果指定了此参数，则不要指定 *Path* 参数。

```yaml
Type: String[]
Parameter Sets: UidParameterSet
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### DfsrIdRecord

## 备注

## 相关链接

[ConvertFrom-DfsrGuid](./ConvertFrom-DfsrGuid.md)

