---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/install-rmsmfgsupport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-RmsMfgSupport
---

# 安装 RmsMfgSupport

## 摘要
为AD RMS服务器添加对Microsoft Federation Gateway的支持。

## 语法

```
Install-RmsMfgSupport [-Force] [-FederationUrl <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Install-RmsMfgSupport` 这个 cmdlet 为 Active Directory 权限管理服务（AD RMS）服务器添加了对 Microsoft Federation Gateway 的支持。

## 示例

### 示例 1：添加对 Microsoft Federation Gateway 的支持
```
PS C:\> Install-RmsMfgSupport
```

此命令为 AD RMS 服务器添加对 Microsoft Federation Gateway 的支持。

## 参数

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -FederationUrl
指定 AD RMS 服务器用于连接 Microsoft Federation Gateway 的统一资源定位符（URL）。如果未指定此参数，AD RMS 将使用默认值连接到 Microsoft Federation Gateway。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需询问用户的确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注
* Before adding Microsoft Federation Gateway Support, it is very important that you back up the AD RMS configuration database.
* Do not run this command if the AD RMS snap-in is open in the Microsoft Management Console (MMC). If you do, the command will not respond until you close the AD RMS MMC snap-in.
* Before uninstalling Service Pack 1 for Windows® 7, you must remove Microsoft Federation Gateway Support from the AD RMS cluster by running the **Uninstall-RmsMfgSupport** cmdlet. Failure to do so may cause an inconsistent configuration of your AD RMS cluster.

## 相关链接

[如何将 Windows PowerShell 与 AD RMS 配合使用](https://go.microsoft.com/fwlink/?LinkId=136806)

