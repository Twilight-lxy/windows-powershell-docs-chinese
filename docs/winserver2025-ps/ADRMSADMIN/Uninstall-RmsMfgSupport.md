---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/uninstall-rmsmfgsupport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-RmsMfgSupport
---

# 卸载 RmsMfgSupport

## 摘要
从AD RMS服务器中移除对Microsoft Federation Gateway的支持。

## 语法

```
Uninstall-RmsMfgSupport [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Uninstall-RmsMfgSupport` cmdlet 用于从 Active Directory 权限管理服务（AD RMS）服务器中删除对 Microsoft Federation Gateway 的支持。

## 示例

#### 示例 1：强制移除对 Microsoft Federation Gateway 的支持
```
PS C:\> Uninstall-RmsMfgSupport -Force
```

此命令强制移除对 AD RMS 的 Microsoft Federation Gateway 支持。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -Force
强制完成当前操作。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注
* Before uninstalling Service Pack 1 for Windows Server® 2008 R2, you must remove Microsoft Federation Gateway Support from the AD RMS cluster. Failure to do this may cause an inconsistent configuration of your AD RMS cluster.

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[安装RMS制造商支持功能](./Install-RmsMfgSupport.md)

