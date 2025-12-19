---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/get-kdsconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-KdsConfiguration
---

# 获取 KDS 配置信息

## 摘要
从 Active Directory 中检索 Microsoft Group KdsSvc 的当前配置信息。

## 语法

```
Get-KdsConfiguration [<CommonParameters>]
```

## 描述
`Get-KdsConfiguration` cmdlet 从 Active Directory 中检索 Microsoft 组密钥分发服务（KdsSvc）的当前配置。KDS 配置定义了如何从根密钥生成其他密钥。

## 示例

### 示例 1：获取当前的 KDS 配置
```
PS C:\> Get-KdsConfiguration
```

此命令从 Active Directory 中检索 Microsoft Group KdsSvc 的当前配置信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
此 cmdlet 不接受任何输入对象。

## 输出

### Microsoft.KeyDistributionService.KdsServerConfiguration
此cmdlet返回一个**KdsServerConfiguration**对象，其中包含用于密钥生成的关键派生函数（KDF）算法和秘密协商算法等信息。

## 备注

## 相关链接

[Add-KdsRootKey](./Add-KdsRootKey.md)

[Clear-KdsCache](./Clear-KdsCache.md)

[Get-KdsRootKey](./Get-KdsRootKey.md)

[Set-KdsConfiguration](./Set-KdsConfiguration.md)

[测试 KDS Root Key](./Test-KdsRootKey.md)

