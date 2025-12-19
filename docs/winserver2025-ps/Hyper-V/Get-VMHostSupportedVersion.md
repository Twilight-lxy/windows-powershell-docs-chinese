---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostsupportedversion?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostSupportedVersion
---

# 获取 VMHost 支持的版本

## 摘要
返回主机支持的虚拟机配置版本列表。

## 语法

### ComputerName（默认值）
```
Get-VMHostSupportedVersion [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [-Default]
 [<CommonParameters>]
```

### CimSession
```
Get-VMHostSupportedVersion [-CimSession] <CimSession[]> [-Default] [<CommonParameters>]
```

## 描述
`Get-VMHostSupportedVersion` cmdlet 会返回一个列表，其中包含该主机支持的虚拟机配置版本。

## 示例

### 示例 1：返回一个支持配置的表格
```
PS C:\> Get-VMHostSupportedVersion
```

此命令返回一个表格，显示该主机上支持的虚拟机配置版本信息。

### 示例 2：返回默认配置版本
```
PS C:\> Get-VMHostSupportedVersion -Default
```

此命令返回该主机的默认虚拟机配置版本。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于运行该cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定域名进行指定。默认值是本地计算机。可以使用“localhost”或点（.“”）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Credential
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Default
指定该 cmdlet 应返回该主机的默认虚拟机配置版本。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShel.VMHostSupportedVersion

## 备注

## 相关链接

[Get-VMHost](./Get-VMHost.md)

