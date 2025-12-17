---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/restore-adfsfarmbehaviorlevel?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-AdfsFarmBehaviorLevel
---

# 恢复 AdFS 农场行为级别（Restore-AdfsFarmBehaviorLevel）

## 摘要
将农场恢复到之前的行为状态。

## 语法

```
Restore-AdfsFarmBehaviorLevel [-Member <String[]>] [-Credential <PSCredential>] -FarmBehavior <Int32> [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Restore-AdfsFarmBehaviorLevel` cmdlet 可将 Active Directory Federation Services (AD FS) 农场恢复到最近一次调整之前的行为级别。

## 示例

## 参数

### -Credential
用于指定在将 SQL Server 作为策略数据库的 AD FS 架构中运行此 cmdlet 所需的凭据。提供的凭据必须具有每台 AD FS 服务器的管理员权限。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FarmBehavior
指定农场（或服务器群）的行为模式。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Member
指定一个成员数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您确认是否要继续执行。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Invoke-AdfsFarmBehaviorLevelRaise](./Invoke-AdfsFarmBehaviorLevelRaise.md)

[测试-AdfsFarmBehaviorLevelRaise](./Test-AdfsFarmBehaviorLevelRaise.md)

[Test-AdfsFarmBehaviorLevelRestore](./Test-AdfsFarmBehaviorLevelRestore.md)

