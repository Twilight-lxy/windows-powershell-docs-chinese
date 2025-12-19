---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/add-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WmsSystem
---

# Add-WmsSystem

## 摘要
添加了一台可以远程管理的计算机。

## 语法

```
Add-WmsSystem [-ComputerName] <String[]> [-ManagedSystemsType] <ManagedSystemTypes>
 [-Credential] <PSCredential> [<CommonParameters>]
```

## 描述
**Add-WmsSystem** cmdlet 允许本地计算机远程管理已安装了多点（MultiPoint）角色或多点连接器（MultiPoint Connector）的计算机。

## 示例


## 参数

### -ComputerName
指定一个要添加的多点系统（MultiPoint system）主机名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定要添加的计算机的管理员凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedSystemsType
用于指定被管理系统的类型。该参数的可接受值包括：MultiPointServers 和 PersonalComputers。

```yaml
Type: ManagedSystemTypes
Parameter Sets: (All)
Aliases:
Accepted values: MultiPointServers, PersonalComputers

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### string[]
输入是一个包含所有需要启用远程管理的计算机的完全限定主机名称的数组。

## 输出

### WmsSystem
对于每台新增的计算机，系统会返回一个 **WmsSystem** 对象，该对象包含了关于该计算机上多点系统配置和状态的具体信息。

## 备注

## 相关链接

[Get-WmsSystem](./Get-WmsSystem.md)

[Remove-WmsSystem](./Remove-WmsSystem.md)

[重启 WMS 系统](./Restart-WmsSystem.md)

[Search-WmsSystem](./Search-WmsSystem.md)

[Set-WmsSystem](./Set-WmsSystem.md)

[Stop-WmsSystem](./Stop-WmsSystem.md)

