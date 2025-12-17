---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/revoke-adfsproxytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Revoke-AdfsProxyTrust
---

# 撤销 AdfsProxyTrust 的信任关系

## 摘要
撤销对所有为联邦服务（Federation Service）配置的联邦服务器代理（federation server proxies）的信任。

## 语法

```
Revoke-AdfsProxyTrust [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Revoke-AdfsProxyTrust` 这个 cmdlet 通过重置 Federation Service 的信任 ID 来撤销对所有联合服务器代理的信任。在发生攻击或确认存在威胁您的部署环境的情况下，可以使用此 cmdlet 实现安全封锁（即限制某些功能的访问）。该 cmdlet 会立即撤销对所有已配置代理的信任。

## 示例

### 示例 1：撤销信任
```
PS C:\> Revoke-AdfsProxyTrust
```

此命令将撤销当前联邦服务器与其配置的所有联邦服务器代理之间的所有信任关系。

## 参数

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注
* Use this cmdlet only in the event of a security breach in a live deployment. We recommend that, if you want to practice using this cmdlet, you use a test lab environment.

## 相关链接

