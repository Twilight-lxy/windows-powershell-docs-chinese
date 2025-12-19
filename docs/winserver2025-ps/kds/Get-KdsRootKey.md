---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/get-kdsrootkey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-KdsRootKey
---

# Get-KdsRootKey

## 摘要
检索由 Microsoft Group KdsSvc 存储的所有根键值的对列表。

## 语法

```
Get-KdsRootKey [<CommonParameters>]
```

## 描述
`Get-KdsRootKey` cmdlet 会从 Active Directory 中检索每个根密钥的以下信息：

- The root key identifier
- The root key value
- The Microsoft Group Key Distribution Service (KdsSvc)

这些信息是生成由 Microsoft Group KdsSvc 分发的组密钥所必需的。

## 示例

### 示例 1：获取根键值列表
```
PS C:\> Get-KdsRootKey
```

此命令用于检索存储在 Active Directory 中的所有根键值（root key values）的列表。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
此cmdlet不接受任何输入对象。

## 输出

### `System.Collections.Generic.List<KdsRootKey^>`
此cmdlet返回存储在Active Directory中的所有主根密钥的列表。

## 备注

## 相关链接

[Add-KdsRootKey](./Add-KdsRootKey.md)

[Clear-KdsCache](./Clear-KdsCache.md)

[Get-KdsConfiguration](./Get-KdsConfiguration.md)

[Set-KdsConfiguration](./Set-KdsConfiguration.md)

[测试 KDS Root Key](./Test-KdsRootKey.md)

