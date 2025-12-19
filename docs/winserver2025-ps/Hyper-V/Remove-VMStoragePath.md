---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmstoragepath?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMStoragePath
---

# 删除虚拟机存储路径

## 摘要
从存储资源池中移除一条路径。

## 语法

```
Remove-VMStoragePath [-Path] <String[]> [-ResourcePoolName] <String[]> [-ResourcePoolType] <VMResourcePoolType>
 [-Passthru] [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [<CommonParameters>]
```

## 描述
`Remove-VMStoragePath` cmdlet 用于从存储资源池中删除某个路径。

## 示例

#### 示例 1
```
PS C:\> Remove-VMStoragePath -Path D:\Test -ResourcePoolName VHD1 -ResourcePoolType VHD
```

将路径 D:\Test 从 VHD 资源池 VHD1 中移除。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，以便从资源池中删除某个路径。允许使用NetBIOS名称、IP地址或完全合格的域名作为主机标识。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **System.String** 对象传递给管道系统，该字符串表示要从资源池中删除的路径。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定要从存储资源池中删除的路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ResourcePoolName
指定要从其中移除路径的资源池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolType
指定要从其中删除路径的资源池的类型。允许的值有 **VFD**、**ISO** 和 **VHD**。

```yaml
Type: VMResourcePoolType
Parameter Sets: (All)
Aliases:
Accepted values: VHD, ISO, VFD

Required: True
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction和-WarningVariable。有关更多信息，请参阅[关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### System.String
如果指定了 **-PassThru** 参数……

## 备注

## 相关链接

