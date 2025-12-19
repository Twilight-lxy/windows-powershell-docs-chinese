---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/clear-kdscache?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-KdsCache
---

# 清除 KDS 缓存

## 摘要
清除本地计算机的组键缓存。

## 语法

```
Clear-KdsCache [-CacheOwnerSid <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-KdsCache` cmdlet 会清除本地计算机的组键缓存。

本地计算机可以是运行 Microsoft 组密钥分发服务（KdsSvc）的域控制器，也可以是该服务的客户端。

## 示例

### 示例 1：清除群组密钥缓存
```
PS C:\> Clear-KdsCache
```

此命令会清除本地计算机的组密钥缓存。

### 示例 2：清除特定用户的组键缓存
```
PS C:\> Clear-KdsCache -CacheOwnerSid "s-1-1-0"
```

此命令会清除SID为s-1-1-0的用户对应的组键缓存。

## 参数

### -CacheOwnerSid
指定该cmdlet要清除其缓存的用户账户的安全标识符（SID）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
此cmdlet不接受任何输入对象。

## 输出

### 无
这个cmdlet不产生任何输出。

## 备注

## 相关链接

[Add-KdsRootKey](./Add-KdsRootKey.md)

[Get-KdsConfiguration](./Get-KdsConfiguration.md)

[Get-KdsRootKey](./Get-KdsRootKey.md)

[Set-KdsConfiguration](./Set-KdsConfiguration.md)

[Test-KdsRootKey](./Test-KdsRootKey.md)

